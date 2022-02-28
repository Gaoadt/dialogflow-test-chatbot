from df_engine.core.keywords import TRANSITIONS, RESPONSE
from df_engine.core import Context, Actor
import df_engine.labels as lbl
import df_engine.conditions as cnd
import re

plot = {
    "global_flow": {
        "start_node": {
            RESPONSE: "",
            TRANSITIONS: {
                "greeting_node": cnd.regexp(r"hi|hello|whats up")
            }
        },
        "greeting_node": {
            RESPONSE: "Hi there, which dialog you gonna talk?"
        },
        "fallback_node": {
            RESPONSE: "Are u kidding me?",
            TRANSITIONS: {
                lbl.forward(): cnd.regexp(r"yes|yeah|aha|sure", re.I),
                lbl.previous(): cnd.true()
            }
        },
        "goodbye_node": {
            RESPONSE: "Goodbye, then)",
        }
    }
}
actor = Actor(plot, start_label=("global_flow", "start_node"), fallback_label=("global_flow", "fallback_node"))
