from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Artificial Intelligence (AI) has become one of the most influential technologies of the modern era. It enables machines to perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, making decisions, and solving problems. AI is widely used in industries including healthcare, finance, education, and transportation. For example, hospitals use AI to assist in diagnosing diseases, while businesses use it to analyze customer behavior and improve services. As AI continues to evolve, it is creating new opportunities for innovation and productivity across the world.

Despite its many benefits, AI also presents several challenges that must be addressed carefully. Issues such as data privacy, algorithmic bias, and cybersecurity have become major concerns as organizations increasingly rely on intelligent systems. Ensuring that AI is developed and used responsibly requires transparency, ethical guidelines, and proper regulation. Additionally, workers may need to adapt to changing job requirements as automation becomes more common. By balancing technological advancement with ethical considerations, society can maximize the benefits of AI while minimizing its potential risks."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 7  00,
    chunk_overlap = 0
)

chunk = splitter.split_text(text)

print(chunk)
print(chunk[0])