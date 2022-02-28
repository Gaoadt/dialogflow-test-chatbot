from typing import Optional, Union
from plot import plot, actor, Actor, Context


def turn_handler(
    in_request: str, ctx: Union[Context, str, dict], actor: Actor, true_out_response: Optional[str] = None
):
    ctx = Context.cast(ctx)
    ctx.add_request(in_request)
    ctx = actor(ctx)
    out_response = ctx.last_response
    return out_response, ctx

def run_interactive_mode(actor: Actor):
    ctx = {}
    out_response, in_request = "", ""
    while not out_response.lower().startswith("goodbye"):
        in_request = input("You: ")
        out_response, ctx = turn_handler(in_request, ctx, actor)
        print(f"Bot: {out_response}")
        
        

if __name__ == '__main__':
    run_interactive_mode(actor)
