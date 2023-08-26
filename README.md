# SummaLearn: Your Personalized Study Assistant

![SummaLearn Logo](path_to_logo.png)  <!-- Replace 'path_to_logo.png' with the actual path to your logo if you have one -->

**Introducing the Future of Study: SummaLearn!**

Are you overwhelmed by the sheer volume of study materials? Do you find yourself skimming through pages of content, desperately searching for the essence? Look no further! We present SummaLearn - the revolutionary tool designed to supercharge your study sessions.

**Why SummaLearn?**

1. **Persona-Driven Summaries**: No two learners are the same, and neither should their summaries be. With SummaLearn, you have the power to tailor your summaries according to your unique learning style. By simply providing a short description of your study persona, our AI crafts a summary that resonates with YOU.

2. **Ease of Use**: With a simple and intuitive interface, all you need to do is upload your PDF document, describe your persona, and voila! Within moments, you'll have a refined, persona-based summary ready for your perusal.

3. **Accuracy and Efficiency**: Powered by advanced generative AI, SummaLearn ensures that the essence of your content isn't lost in translation. Instead of spending hours trying to condense information, you now have the luxury of getting straight to the point, saving you valuable time.

4. **All Content Types Welcome**: Whether it's a dense academic paper, a lengthy novel, or a technical manual, SummaLearn is equipped to handle it all. Our AI has been trained on a diverse range of topics, ensuring that your summaries are not just concise, but also comprehensive.

5. **Safe and Secure**: We understand the importance of privacy. Rest assured, your uploaded documents remain confidential and are never stored beyond the duration of processing.

**Invest in Your Learning Today!**

In today's fast-paced world, efficient learning is not just a luxury; it's a necessity. SummaLearn bridges the gap between overwhelming content and digestible knowledge. Why trudge through endless pages when you can grasp the core in just a few paragraphs? 

Let SummaLearn be your academic ally. Embrace a smarter, more personalized way of studying. Dive deep into the world of knowledge without feeling buried under it.

Join the study revolution. Experience SummaLearn now!

## Prerequisites:

Make sure you have the following installed:
- Python 3.x
- Streamlit

## Installation:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mgrainger87/SummaLearn.git
   cd SummaLearn
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```
## Generating an OpenAPI API Key:

To use SummaLeaern, you will need an OpenAPI API key. Here's how you can obtain and configure it:

1. **Visit the OpenAPI Registration Portal**:
   - Navigate to [OpenAPI's registration page](https://platform.openai.com/).
   
2. **Sign Up/Log In**:
   - If you're a new user, sign up for an account. If you already have an account, simply log in.

3. **Generate API Key**:
   - Once logged in, go to the 'API Keys' section.
   - Click on 'Generate New Key'. You might be prompted to give your key a name or set permissions. Make sure you grant the required permissions for SummaLearn to function optimally.

**Note**: Keep your API key confidential. Do not share it with others or expose it in public forums. If you believe your key has been compromised, return to the OpenAPI portal and revoke the key, then generate a new one.

## Usage:

1. **Run SummaLearn**:
   ```bash
   streamlit run SummaLearn/summalearn.py
   ```

2. This will launch SummaLearn in your default web browser. Follow the on-screen instructions:
   - Enter your API key.
   - Upload your PDF document.
   - Provide a short description of your study persona.
   - Wait a moment for SummaLearn to generate your personalized summary.
   - Read and utilize the generated summary for your studies!

## Contributing:

We welcome contributions! Please see the `CONTRIBUTING.md` file for guidelines.

## License:

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Support & Feedback:

For any queries or feedback, please raise an issue on our [GitHub repository](https://github.com/mgrainger87/SummaLearn/issues).

Happy Studying with SummaLearn!
