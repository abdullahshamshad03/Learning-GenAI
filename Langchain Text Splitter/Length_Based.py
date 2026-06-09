from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    
)

text = "The rapid advancement of technology has transformed nearly every aspect of modern life, from the way people communicate and learn to how businesses operate and governments provide services. The internet has connected billions of individuals across the globe, enabling instant access to information that was once difficult or impossible to obtain. Students can now attend online courses from leading universities, professionals can collaborate with colleagues in different countries in real time, and entrepreneurs can reach international markets with minimal resources. At the same time, emerging technologies such as artificial intelligence, cloud computing, and data analytics are creating new opportunities for innovation and efficiency. Companies use these tools to automate repetitive tasks, improve customer experiences, and make more informed decisions based on large volumes of data. However, technological progress also brings challenges. Concerns about privacy, cybersecurity, misinformation, and the ethical use of AI have become increasingly important as digital systems become more integrated into daily life. Organizations must balance innovation with responsibility, ensuring that technological solutions are designed and deployed in ways that benefit society as a whole. Furthermore, the rapid pace of change requires individuals to continuously update their skills and adapt to new tools and working methods. Lifelong learning has become a necessity rather than an option in many industries. Despite these challenges, technology remains a powerful force for progress, enabling breakthroughs in healthcare, education, transportation, and scientific research. As societies continue to evolve alongside technological developments, the ability to use these tools effectively and responsibly will play a critical role in shaping a more connected, productive, and sustainable future for generations to come."

chunks = splitter.split_text(text)
print(chunks)