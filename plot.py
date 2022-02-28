from df_engine.core.keywords import TRANSITIONS, RESPONSE
from df_engine.core import Context, Actor
import df_engine.labels as lbl
import df_engine.conditions as cnd


plot = {
    "global_flow": {
        "start_node": {
            RESPONSE: ""
        },
        "fallback_node": {
            RESPONSE: "Are u kidding me?"
        }
    }
}
actor = Actor(plot, start_label=("global_flow", "start_node"), fallback_label=("global_flow", "fallback_node"))
