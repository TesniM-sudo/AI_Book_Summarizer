Text Summarizer 📝

A simple Python application that summarizes text using AI-powered natural language processing. This tool uses the DistilBART model from Hugging Face's Transformers library to generate concise summaries of longer texts.

## Features ✨

- **Offline summarization** - No API keys or internet required after initial setup
- **Free to use** - Uses open-source models
- **Easy to use** - Simple command-line interface
- **Powered by AI** - Uses Facebook's DistilBART model for high-quality summaries

## Prerequisites 📋

- Python 3.8 or higher
- pip (Python package manager)

## Installation 🔧

1. **Clone the repository**
```bash
   git clone https://github.com/YOUR_USERNAME/text-summarizer.git
   cd text-summarizer
```

2. **Create a virtual environment** (recommended)
```bash
   python -m venv .venv
```

3. **Activate the virtual environment**
   - **Windows:**
```bash
     .venv\Scripts\activate
```
   - **Mac/Linux:**
```bash
     source .venv/bin/activate
```

4. **Install dependencies**
```bash
   pip install -r requirements.txt
```

   **Note:** First run will download the model (~500MB). This only happens once.

## Usage 🚀

Run the script:
```bash
python summarize.py
```

When prompted, paste your text and press Enter. The summarized version will appear below.

### Example

**Input:**
The rising popularity of electric vehicles marks a significant shift in the automotive
industry. In view of global efforts to reduce carbon emissions and growing concerns about
climate change, battery-powered cars represent a promising alternative to conventional
combustion engines. Although initial challenges like limited range and the necessary
expansion of the charging infrastructure exist, governments worldwide are promoting the
transition through subsidies and tax incentives.

**Output:**
Electric vehicles represent a shift in the automotive industry as governments promote
the transition with subsidies. Battery-powered cars are a promising alternative to
conventional engines despite challenges like limited range and charging infrastructure.

## Project Structure 📁
text-summarizer/
├── summarize.py          # Main application script
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── README.md            # This file

## Dependencies 📦

- `transformers` - Hugging Face Transformers library
- `torch` - PyTorch (deep learning framework)

Install all dependencies with:
```bash
pip install transformers torch
```

Or create a `requirements.txt`:
transformers>=4.30.0
torch>=2.0.0

## How It Works 🔍

The application uses the **DistilBART** model, a distilled (smaller, faster) version of Facebook's BART model:

1. Loads the pre-trained summarization model from Hugging Face
2. Takes your input text
3. Processes it through the model
4. Returns a concise summary

The model runs entirely on your local machine - no API calls or internet required after the initial download.

## Troubleshooting 🛠️

### Model download is slow
- The first run downloads ~500MB. Be patient!
- Ensure you have a stable internet connection
- Progress might not always be visible

### Out of memory errors
- Try summarizing shorter texts
- Close other applications to free up RAM

### Import errors
- Make sure you've activated your virtual environment
- Run `pip install -r requirements.txt` again

## Customization ⚙️

You can adjust summary length in `summarize.py`:
```python
summary = summarizer(
    text, 
    max_length=100,   # Maximum summary length
    min_length=25,    # Minimum summary length
    do_sample=False
)
```

## Future Improvements 🚧

- [ ] Add GUI interface
- [ ] Support for multiple languages
- [ ] Batch processing of multiple texts
- [ ] Export summaries to file
- [ ] Web interface

## Contributing 🤝

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License 📄

This project is open source and available under the MIT License.

## Acknowledgments 🙏

- [Hugging Face](https://huggingface.co/) for the Transformers library
- Facebook AI for the BART model
- [DistilBART model](https://huggingface.co/sshleifer/distilbart-cnn-12-6) by Sam Shleifer

## Author ✍️

**Bahrouni Tesnim** - Software engineering and information systems Student at UIT, specializing in AI 

---

⭐ If you found this helpful, consider giving it a star!

Also Create This File: requirements.txt
transformers>=4.30.0
torch>=2.0.0
