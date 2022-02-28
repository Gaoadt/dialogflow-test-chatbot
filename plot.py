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
            RESPONSE: "What would you like to eat?",
            TRANSITIONS:{
                ("pizza_flow", "init"): cnd.regexp("pizza|some pizza"),
                ("burger_flow", "init"): cnd.regexp("burger|big tasty burger"),
                lbl.repeat(): cnd.regexp("what|don't understand you|repeat")
            }
        },
        "fallback_node": {
            RESPONSE: "Are u kidding me?",
            TRANSITIONS: {
                lbl.forward(): cnd.regexp(r"yes|yeah|aha|sure"),
                lbl.previous(): cnd.true()
            }
        },
        "goodbye_node": {
            RESPONSE: "Goodbye, then)",
        }
    },

    "pizza_flow":{
        "init":{
            RESPONSE: "Okay, we serve margaritas and havanians, which pizza would you like ^-^ ?",
            TRANSITIONS: {
                lbl.forward(): cnd.regexp("margarita"),
                "havanian": cnd.regexp("havanian"),
                lbl.repeat(): cnd.regexp("what|don't understand you|repeat")
            }
        },
        "margarita":{
            RESPONSE: "Enjoy your tasty margarita",
            TRANSITIONS: {
                ("global_flow", "greeting_node"): cnd.true(),
                lbl.repeat(): cnd.regexp("what|don't understand you|repeat")
            }
        },
        "havanian":{
            RESPONSE: "Goodbye, I don't talk to that pineaple eaters"
        }
    },
    "burger_flow":{
        "init":{
            RESPONSE: "Hm, cheeseburger or hamburger",
            TRANSITIONS: {
                 "done": cnd.regexp("cheeseburger|hamburger"),
                 lbl.repeat(): cnd.regexp("what|don't understand you|repeat")
            }
        },
        "done":{
            RESPONSE: "Here you are) ..",
            TRANSITIONS :{
                ("global_flow", "greeting_node"): cnd.true(),
                lbl.repeat(): cnd.regexp("what|don't understand you|repeat")
            }
        }
    }
    
}
actor = Actor(plot, start_label=("global_flow", "start_node"), fallback_label=("global_flow", "fallback_node"))
