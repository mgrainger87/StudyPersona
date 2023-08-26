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

## Powered by DemoGPT

SummaLearn is proud to be built on the foundation of DemoGPT, an innovative open-source project that crafts applications using cutting-edge generative AI from just a single prompt. This testament to the power of AI showcases how technology can be harnessed to create functional and impactful applications with minimal human input.

For those curious about DemoGPT or interested in creating their own applications using this revolutionary technology, visit the official [DemoGPT website](https://www.demogpt.io).

By leveraging the capabilities of DemoGPT, SummaLearn aims to provide the best in class service for students, ensuring quality and efficiency in every generated summary.

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
## Generating an OpenAI API Key:

For enhanced functionality, SummaLearn integrates with OpenAI's powerful models. To utilize these features, you'll need an OpenAI API key. Follow these steps to obtain and configure it:

1. **Visit OpenAI's Developer Portal**:
   - Navigate to [OpenAPI's Developer Dashboard](https://platform.openai.com/).
   
2. **Sign Up/Log In**:
   - If you're a new user, sign up for an account. Existing users can log in.

3. **Generate API Key**:
   - Once logged in, head to the 'API Keys' section.
   - Click on 'Create a New Key'. Assign the necessary permissions and provide a name for the key if prompted.

**Important**: Your API key is sensitive information. Do not share it publicly, and avoid committing it directly to source code repositories. If you believe your key has been compromised, revisit the OpenAI portal to revoke the key and generate a new one.

## Usage:

1. **Run SummaLearn**:
   ```bash
   streamlit run summalearn.py
   ```

2. This will launch SummaLearn in your default web browser. Follow the on-screen instructions:
   - Enter your API key.
   - Upload your PDF document.
   - Provide a short description of your study persona.
   - Wait a moment for SummaLearn to generate your personalized summary.
   - Read and utilize the generated summary for your studies!

## Sample Personas

Here are some persona descriptions that can guide the AI in tailoring summaries:

1. **Interactive Learner**: "Add interactive elements or quizzes in the summary."
2. **Ethical Examiner**: "Emphasize ethical considerations or moral implications in the summary."
3. **Quick Reviser**: "Provide a brief, bullet-point summary for quick revision."
4. **Deep Diver**: "Craft a detailed summary covering all major points."
5. **Conceptual Thinker**: "Emphasize core concepts and theories in the summary."
6. **Practical Implementer**: "Highlight practical applications and real-world examples."
7. **Question Seeker**: "Format the summary as a Q&A."
8. **Historical Contextualizer**: "Incorporate historical context and background in the summary."
9. **Future Predictor**: "Include speculations on future implications of the topic."
10. **Analogy Lover**: "Use comparisons and metaphors for explanations."
11. **Cultural Explorer**: "Integrate cultural, societal, or global perspectives in the summary."
12. **Debater**: "Present multiple viewpoints or arguments in the summary."
13. **Storyteller**: "Narrate the summary in a story format."
15. **Flashcard Fan**: "Segment the summary into flashcard-friendly snippets."
16. **Project Planner**: "Detail the steps, stages, or processes in the summary."

These personality-based personas can add unique flavors and perspectives to the generated summaries, making them engaging and entertaining:

1. **Pirate**: "Craft the summary as if spoken by a swashbuckling pirate seeking treasure."
2. **Criminal**: "Frame the summary with a sneaky, cunning tone, as if planning a heist."
3. **Royalty**: "Present the summary with elegance and grandeur, fit for a king or queen."
4. **Animal**: "Narrate the summary from the perspective of a curious animal exploring its environment."
5. **Knight**: "Write the summary with valor and honor, as if preparing for a noble quest."
6. **Witch/Wizard**: "Infuse the summary with a magical and mystical tone, hinting at spells and potions."
7. **Explorer**: "Detail the summary with wonder and discovery, like an adventurer charting unknown lands."
8. **Alien**: "Provide a summary from the viewpoint of an extraterrestrial observing Earth for the first time."
9. **Robot**: "Generate a summary in a logical and analytical manner, devoid of emotion."
10. **Ghost**: "Craft the summary with an eerie, haunting tone, as if whispered from the beyond."
11. **Viking**: "Write with the vigor and might of a Viking setting sail for conquest."
12. **Detective**: "Frame the summary as clues and findings from a complex investigation."
13. **Noble**: "Present the summary with politeness and decorum, as befitting a highborn."
14. **Scientist**: "Detail the summary with precision and curiosity, emphasizing facts and discoveries."
15. **Mystic**: "Infuse the summary with spiritual and ethereal insights, hinting at deeper truths."
16. **Warrior**: "Craft the summary with determination and courage, ready for battle."
17. **Minstrel**: "Narrate the summary in a poetic and lyrical manner, suitable for a song or ballad."
18. **Traveler**: "Write the summary with tales and observations from a journey across diverse landscapes."
19. **Child**: "Provide a summary with innocence and wonder, as seen through a child's eyes."
20. **Elder**: "Generate the summary with wisdom and experience, sharing tales from the past."

## Contributing:

We welcome contributions! Please see the `CONTRIBUTING.md` file for guidelines.

## Support & Feedback:

For any queries or feedback, please raise an issue on our [GitHub repository](https://github.com/mgrainger87/SummaLearn/issues).

Happy Studying with SummaLearn!
