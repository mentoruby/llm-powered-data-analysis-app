import datetime
import streamlit as st

def show_generate_report_button():
    st.sidebar.markdown("---")
    st.sidebar.header("Export Options")
    if st.sidebar.button("Generate Report"):
        export_html = export_conversation()
        if export_html is not None:
            st.sidebar.download_button(
                label="Download Report (HTML)",
                data=export_html,
                file_name=f"data_analysis_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.html",
                mime="text/html"
            )
            st.sidebar.info("Tip: Open the HTML file and print to PDF for best results")
        else:
            st.sidebar.info("Tip: No chat history for reporting")

# Helper function for export
def export_conversation():
    if not st.session_state.messages:
        return None
    # Create HTML content with embedded styles
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #333; }}
            h2 {{ color: #666; margin-top: 30px; }}
            h3 {{ color: #888; margin-top: 20px; }}
            .question {{ background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin: 10px 0; }}
            .answer {{ padding: 10px; margin: 10px 0; }}
            .metadata {{ color: #999; font-size: 14px; }}
            code {{ background-color: #f5f5f5; padding: 2px 4px; border-radius: 3px; }}
            pre {{ background-color: #f5f5f5; padding: 10px; border-radius: 5px; overflow-x: auto; }}
        </style>
    </head>
    <body>
        <h1>Data Analysis Report</h1>
        <p class="metadata">Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
    """

    # Add data summary
    if st.session_state.df is not None:
        html_content += f"""
        <h2>Dataset Information</h2>
        <ul>
            <li>Total Rows: {st.session_state.df.shape[0]}</li>
            <li>Total Columns: {st.session_state.df.shape[1]}</li>
            <li>Column Names: {', '.join(st.session_state.df.columns)}</li>
        </ul>
        """

    # Add conversation
    html_content += "<h2>Analysis Conversation</h2>"
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            html_content += f'<div class="question"><strong>Question:</strong> {msg["content"]}</div>'
        else:
            # Convert markdown code blocks to HTML
            content = msg["content"].replace("```python", "<pre><code>").replace("```", "</code></pre>")
            html_content += f'<div class="answer"><strong>Analysis:</strong><br>{content}</div>'
            if "figure" in msg:
                html_content += '<p><em>[Visualization generated - see application for details]</em></p>'

    html_content += """
    </body>
    </html>
    """

    return html_content