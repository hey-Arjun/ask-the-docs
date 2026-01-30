import gradio as gr
import requests

BACKEND_URL = "http://100.31.112.111:8000"

def upload_file(file):
    global uploaded
    if file is None:
        return "No file selected"
    files = {
        "file": (file, open(file, "rb"))
    }

    response = requests.post(
        f"{BACKEND_URL}/upload",
        files = files
    )

    if response.status_code == 200:
        uploaded = True
        return "Document uploaded successfully"
    else:
        return "Upload failed"

def ask_question(question):
    payload = {
        "question": question
    }
    
    response = requests.post(
        f"{BACKEND_URL}/ask",
        params = payload
    )

    data = response.json()
    if "error" in data:
        return data["error"], ""

    return data["answer"], "\n\n".join(data.get("sources", []))





with gr.Blocks(title="Ask the Docs") as demo:

    gr.Markdown("### 📤 Upload Document")

    file_input = gr.File(
        label="Document (PDF / TXT)",
        file_types=[".pdf", ".txt"]
    )

    upload_btn = gr.Button("Upload")

    upload_status = gr.Textbox(label="Status")

    upload_btn.click(
        fn=upload_file,
        inputs=file_input,
        outputs=upload_status
    )

    gr.Markdown("")

    gr.Markdown("### ❓ Ask Question")

    question_input = gr.Textbox(
        placeholder="Ask something from the document...",
        label="Your Question",
        lines=2
    )

    ask_btn = gr.Button("Ask")

    gr.Markdown("")

    gr.Markdown("### ✅ Answer")

    answer_output = gr.Textbox(
        label="Answer",
        lines=10,
    )
    gr.Markdown("")

    with gr.Accordion("Sources", open=False):
        sources_output = gr.Textbox(lines=8)

    ask_btn.click(
        fn=ask_question,
        inputs=question_input,
        outputs=[answer_output, sources_output]
    )


demo.launch(server_name="0.0.0.0", server_port=7860, theme=gr.themes.Soft())


