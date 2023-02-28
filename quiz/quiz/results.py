import pynecone as pc

results_style = {
    "bg": "white",
    "padding_x": "5rem",
    "padding_y": "2em", #padding top, bottom 각 2em 씩
    "border_radius": "25px",
    "align_items": "left",
    "overflow": "auto",
}
columns = ["#", "RESULT", "YOUR ANSWER", "CORRECT ANSWER"]

def circle(score):
    return pc.center(
        pc.circular_progress(
            pc.circular_progress_label(score), value=score
        ),
    )

def render_answer(state, index):
    return pc.tr(
        pc.td(index + 1),
        pc.td(
            pc.cond(
                state.answers[index].to_string() == state.answers_key[index].to_string(),
                pc.icon(tag="add"),
                pc.icon(tag="minus"),
            )
        ),
        pc.td(state.answers[index].to_string()),
        pc.td(state.answers_key[index].to_string()),
    )

def table(state):
    return pc.table(
        pc.thead(
            pc.tr(
                pc.th("#"),
                pc.th("Result"),
                pc.th("Your Answer"),
                pc.th("Correct Answer"),
            )
        ),
        pc.tbody(
            pc.foreach(state.answers, lambda answer, i: render_answer(state, i)),
        )
    )

def results(State):
    state = State
    return pc.center(
        pc.vstack(
            pc.heading("Results"),
            pc.text("Below are the results of the quiz."),
            pc.divider(),
            circle(state.score),
            table(state),
            bg="white",
            padding_x="5em",
            padding_y="2em",
            border_radius="25px",
            align_items="left",
            overflow="auto",
        ),
        bg="#edededed",
        height="100vh",
        align_items="top",
        padding="1em",
        overflow="auto",
        #style = results_style,
    )