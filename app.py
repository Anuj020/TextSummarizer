import gradio as gr
import openai

# Set your OpenAI API key here
openai.api_key = "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"

def generate_summary(text_input):
    prompt = f"Summarize the following text:\n\n{text_input}\n\nSummary:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100  # Adjust this to control the summary length
    )
    summary = response.choices[0].text.strip()
    return summary

iface = gr.Interface(
    fn=generate_summary,
    inputs=gr.inputs.Textbox(lines=10, placeholder="Paste the text you want to summarize..."),
    outputs="text",
    title="Text Summarizer",
    description="Enter a longer text and get a summarized version."
)
iface.launch()
