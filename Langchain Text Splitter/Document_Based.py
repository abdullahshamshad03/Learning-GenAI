from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

text = """# Artificial Intelligence

Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think, learn, and make decisions. AI is transforming industries and changing the way people interact with technology.

## History of AI

The concept of AI dates back to the 1950s when researchers first began exploring the possibility of creating machines that could mimic human reasoning. Over the decades, advancements in computing power and data availability have accelerated AI development.

## Applications of AI

AI has found applications in numerous fields and continues to expand into new domains.

### Healthcare

AI-powered systems can assist doctors in diagnosing diseases, analyzing medical images, and predicting patient outcomes. These technologies help improve the quality and efficiency of healthcare services.

### Education

Educational platforms use AI to personalize learning experiences. Intelligent tutoring systems can adapt content and provide customized recommendations based on a student's progress.

### Finance

Financial institutions use AI for fraud detection, risk assessment, algorithmic trading, and customer support. AI helps organizations process large volumes of financial data efficiently.

## Challenges

Despite its benefits, AI presents several challenges that require careful consideration.

### Privacy Concerns

AI systems often rely on large datasets, raising concerns about how personal information is collected, stored, and used.

### Bias and Fairness

Machine learning models can inherit biases present in training data, potentially leading to unfair or discriminatory outcomes.

### Security Risks

As AI systems become more widespread, protecting them from cyberattacks and misuse becomes increasingly important.

## Future of AI

The future of AI is expected to bring significant advancements in automation, scientific research, and human-computer interaction. Responsible development and ethical guidelines will play a crucial role in ensuring that AI benefits society.

# Conclusion

Artificial Intelligence is a powerful technology with the potential to solve complex problems and improve many aspects of daily life. While challenges remain, continued research and responsible implementation can help maximize its positive impact."""

splitters = RecursiveCharacterTextSplitter.from_language(
    language = Language.MARKDOWN,
    chunk_size = 300,
    chunk_overlap = 0
)

chunks = splitters.split_text(text)
print(chunks)