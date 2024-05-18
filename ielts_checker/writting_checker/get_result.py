import google.generativeai as genai

genai.configure(api_key="AIzaSyAFejakqWRITENoOl5qSDxFQNCqiPdBxak")

generation_config = {
    'temperature' : 0,
    'top_p' : 1,
    'top_k' : 1,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]
essay_prompt_1 = """
## Input :
**Topic**
It is a natural process for animal species to become extinct (e.g. Dinosaur, dodos …) There is no reason why people should try to prevent this from happening. Do you agree or disagree?
**Assignment**
Certain individuals hold the belief that there are no compelling reasons for us to protect animal species from extinction as it occurs naturally. I dissent with this conviction and will support my argument in the essay below.
It is true that millions of years ago, many ancient species of animals, such as dinosaurs, were wiped out due to a gradual shift in climate and changing sea levels, according to some hypotheses. However, these environmental factors are not the primary contributor to the disappearance of certain species nowadays. Industrial activities have been devastating the natural habitats of wildlife and disturbing the food chain, causing the mass extinction  of countless species. The increased demand for goods made from animals’ products, such as skins and horns, also leads to the rampant poaching of wild, endangered animals, rhinos for instance. In this regard, humans are held accountable and should do what is needed to rectify the situation.
Other justifications  for saving wild animals involve  the significant roles that they play in not only the balance of the ecosystem but also our lives. Everything in nature is connected , and if one species becomes extinct, many other animals and even plants will suffer as the food chain is disrupted. Wild animals also have great aesthetic and socio-cultural values. They contribute to our rich bio-diversity  that makes this planet a beautiful place. In numerous places around the world, many types of animals play an important role in different cultures. For example, in some religions, cows are revered and worshiped as gods.
The disappearance of many animal species does not always occur as a natural process but as a consequence of our doings . It is our obligation to help preserve wild animals because their extinction will have a severe influence on many important aspects of our lives.

## Feedback :
**Vocabulary and Grammar Enhancement**
-   some people believe-> certain individuals hold the belief
Explanation: Replacing "some people believe" with "certain individuals hold the belief" elevates the language by using more formal terminology and avoids the use of colloquial language.
-   the mass extinction-> the widespread extinction
Explanation: Replacing "the mass extinction" with "the widespread extinction" offers a more precise term that aligns better with academic language.
-   Other justifications-> Additional rationales
Explanation: "Other justifications" can be replaced with "Additional rationales" to enhance the formality and specificity of the language.
-   involve-> include
Explanation: Substituting "involve" with "include" provides a more formal and precise term that fits academic writing conventions.
-   Everything in nature is connected-> The interconnectedness of nature
Explanation: Rewording "Everything in nature is connected" to "The interconnectedness of nature" maintains the meaning while using more sophisticated language.
-   rich bio-diversity-> rich biodiversity
Explanation: "Bio-diversity" can be corrected to "biodiversity" to adhere to standard spelling conventions in academic writing.
-   does not always occur as a natural process but as a consequence of our doings-> does not always result from natural processes but from human actions
Explanation: The phrase "as a consequence of our doings" can be replaced with "from human actions" to convey the same meaning in a more formal manner.

**Strengthening the Argument**
-   Introduction: "Some people believe that there are no compelling reasons for us to protect animal species from extinction as it occurs naturally. I personally disagree with this conviction and will support my argument in the essay below.
    +	Explanation: The introduction clearly states the writer's position on the issue and sets the stage for the discussion to follow.
    +	Improved Example: "While some argue that the natural extinction of animal species is a necessary part of evolution, I firmly believe that we have a moral and ethical obligation to protect these species from extinction. This essay will explore the reasons why preventing animal extinction is not only important for the preservation of biodiversity but also for the well-being of our planet and future generations."
-	Main Point 1: "It is true that millions of years ago, many ancient species of animals, such as dinosaurs, were wiped out due to a gradual shift in climate and changing sea levels, according to some hypotheses. However, these environmental factors are not the primary contributor to the disappearance of certain species nowadays. Industrial activities have been devastating the natural habitats of wildlife and disturbing the food chain, causing the mass extinction of countless species.
    +	Explanation: This point effectively highlights the role of human activities in the current extinction crisis.
    +	Improved Example: "While it is true that natural factors such as climate change and sea level rise have contributed to the extinction of species in the past, the current extinction crisis is primarily driven by human activities. The destruction of natural habitats, pollution, and climate change have disrupted ecosystems and endangered countless species."
-	Main Point 2: "The increased demand for goods made from animals’ products, such as skins and horns, also leads to the rampant poaching of wild, endangered animals, rhinos for instance. In this regard, humans are held accountable and should do what is needed to rectify the situation.
    +	Explanation: This point effectively addresses the role of human consumption in the extinction of certain species.
    +	Improved Example: "The demand for animal products such as meat, fur, and ivory has led to rampant poaching and the exploitation of endangered species. The illegal wildlife trade is a major contributor to the extinction of many species, and it is our responsibility to curb this trade and protect these animals."
-	Main Point 3: "Other justifications for saving wild animals involve the significant roles that they play in not only the balance of the ecosystem but also our lives. Everything in nature is connected, and if one species becomes extinct, many other animals and even plants will suffer as the food chain is disrupted. Wild animals also have great aesthetic and socio-cultural values. They contribute to our rich bio-diversity that makes this planet a beautiful place. In numerous places around the world, many types of animals play an important role in different cultures. For example, in some religions, cows are revered and worshiped as gods.
    +	Explanation: This point effectively highlights the ecological and cultural significance of wild animals.
    +	Improved Example: "Wild animals play a crucial role in maintaining the balance of ecosystems. They are essential for pollination, seed dispersal, and nutrient cycling. The loss of even a single species can have a ripple effect on the entire ecosystem. Additionally, wild animals have cultural and aesthetic value. They inspire art, literature, and spiritual practices. The extinction of these animals would be a loss to humanity's cultural heritage."
-	Conclusion: "The disappearance of many animal species does not always occur as a natural process but as a consequence of our doings. It is our obligation to help preserve wild animals because their extinction will have a severe influence on many important aspects of our lives.
    +	Explanation: The conclusion effectively summarizes the main arguments and reiterates the writer's position.
    +	Improved Example: "In conclusion, while natural factors may have contributed to the extinction of species in the past, the current extinction crisis is primarily driven by human activities. It is our responsibility to protect these animals and their habitats. The loss of biodiversity, the disruption of ecosystems, and the cultural significance of wild animals make it imperative that we take action to prevent animal extinction."
Overall, the essay provides a well-reasoned and persuasive argument against the idea that animal species should be allowed to go extinct naturally. The writer effectively highlights the role of human activities in the current extinction crisis and the ecological, cultural, and ethical significance of wild animals.
**Task Response**
Band Score for Task Response: 8
-	Answer All Parts of the Question:
    +	Detailed explanation: The essay adequately addresses all parts of the question. It acknowledges the premise that extinction is a natural process and presents a clear disagreement with the notion that there is no reason to prevent it.
    +	How to improve: While the essay does well in addressing all parts of the question, providing specific examples or statistics to illustrate the impact of human activities on species extinction could strengthen the argument further.
-	Present a Clear Position Throughout:
    +	Detailed explanation: The essay maintains a clear and consistent position throughout, firmly disagreeing with the idea that humans should not try to prevent animal species from becoming extinct. The stance is evident from the introduction to the conclusion.
    +	How to improve: To enhance clarity, ensure that each paragraph reinforces the central argument and avoids any ambiguous language that might obscure the position.
-	Present, Extend, and Support Ideas:
    +	Detailed explanation: The essay effectively presents, extends, and supports ideas. It provides examples of human activities contributing to species extinction, such as industrial activities and poaching, and elaborates on the importance of preserving wildlife for ecological balance and cultural significance.
    +	How to improve: To further develop ideas, consider incorporating counterarguments and refutations to strengthen the overall argumentation.
-	Stay on Topic:
    +	Detailed explanation: The essay remains focused on the topic throughout, discussing reasons why it is essential for humans to prevent animal species from becoming extinct. It does not deviate into tangential discussions.
    +	How to improve: To maintain focus, ensure that each paragraph directly relates to the central argument and avoids introducing unrelated ideas or information.
Overall, while the essay effectively addresses the prompt, incorporating more specific examples, reinforcing clarity, developing ideas with counterarguments, and maintaining focus could enhance the overall coherence and persuasiveness of the argument.
**Coherence & Cohesion**
Band Score for Coherence and Cohesion: 7
-	Organize Information Logically:
    +	Detailed explanation: The essay demonstrates a generally logical organization of ideas. It begins with a clear introduction that outlines the writer's stance on the issue. Each subsequent paragraph presents a distinct argument supported by examples and reasoning. The progression from discussing the natural extinction process to human-induced factors is coherent and easy to follow.
    +	How to improve: To enhance logical organization further, consider refining transitions between paragraphs to ensure a seamless flow of ideas. Additionally, maintaining a consistent level of depth in argumentation throughout the essay can bolster coherence.
-	Use Paragraphs:
    +	Detailed explanation: The essay effectively utilizes paragraphs to structure its content. Each paragraph addresses a specific aspect of the argument, such as the causes of extinction and the importance of preserving wildlife. The opening and closing paragraphs appropriately introduce and conclude the essay, respectively.
    +	How to improve: To further improve paragraphing, ensure that each paragraph maintains a clear focus on its central idea and provides sufficient elaboration. Consider varying sentence structures within paragraphs to enhance readability and engagement.
-	Use a Range of Cohesive Devices:
    +	Detailed explanation: The essay employs a variety of cohesive devices to connect ideas and maintain coherence. For instance, cohesive devices such as 'however' and 'in this regard' are used to signal transitions between contrasting or related points. Additionally, pronouns and demonstrative adjectives help establish coherence by referring back to previously mentioned concepts.
    +	How to improve: While cohesive devices are utilized effectively overall, consider incorporating a broader range of transitions and connectors to further enhance coherence. Introducing more advanced cohesive devices, such as conditional clauses or concessive adverbs, can add sophistication to the essay's structure and improve clarity.
Overall, the essay demonstrates a strong grasp of coherence and cohesion, earning a band score of 7. To continue improving, focus on refining transitions between paragraphs, maintaining clarity and depth in argumentation, and diversifying the use of cohesive devices. With continued practice and attention to these areas, the essay's coherence and cohesion can reach an even higher level.
**Lexical Resource**
Band Score for Lexical Resource: 7
-	Use a Wide Range of Vocabulary:
    +	Detailed explanation: The essay demonstrates a commendable breadth of vocabulary. For instance, the writer employs a variety of terms such as "extinction," "devastating," "rampant," "bio-diversity," and "revered," showcasing an ability to express ideas using diverse lexical choices.
    +	How to improve: While the essay displays a strong vocabulary, enhancing the sophistication of language further can elevate the lexical resource score. Integrating more advanced vocabulary and idiomatic expressions relevant to the topic can enrich the essay's language and boost its lexical resource band score.
-	Use Vocabulary Precisely:
    +	Detailed explanation: The vocabulary usage in the essay is generally precise and effective. For instance, terms like "industrial activities," "natural habitats," and "food chain" are employed accurately to convey the intended meanings.
    +	How to improve: To refine precision, it's advisable to avoid overused or generic terms. In specific instances, substituting common words with more nuanced synonyms or technical vocabulary can enhance precision. Additionally, maintaining consistency in terminology usage throughout the essay can further improve clarity and precision.
-	Use Correct Spelling:
    +	Detailed explanation: The essay demonstrates a satisfactory level of spelling accuracy, with no glaring errors detracting from comprehension.
    +	How to improve: To ensure consistent spelling accuracy, utilizing spell-checking tools and proofreading thoroughly before submission can be beneficial. Additionally, actively practicing spelling through activities such as word games or vocabulary drills can help reinforce correct spelling habits over time.
**Grammatical Range & Accuracy**
Band Score for Grammatical Range and Accuracy: 7
-	Use a Wide Range of Structures:
    +	Detailed explanation: The essay demonstrates a commendable range of sentence structures, including complex and compound sentences. For instance, the writer effectively employs complex sentences to articulate ideas: "Industrial activities have been devastating the natural habitats of wildlife and disturbing the food chain, causing the mass extinction of countless species." This construction combines multiple clauses to convey a detailed argument. Additionally, there are instances of relative clauses ("such as dinosaurs"), conditional sentences ("if one species becomes extinct"), and phrases used for emphasis and clarification ("according to some hypotheses"). These varied structures enhance the overall coherence and sophistication of the essay.
    +	How to improve: To further enhance grammatical range, consider integrating more advanced structures such as reduced adjective clauses ("wild animals being essential"), passive voice constructions ("are held accountable"), or inversion for emphasis ("Not only does this affect..."). Additionally, incorporating rhetorical devices like parallelism and ellipsis can add stylistic flair to the writing.
-	Use Grammar and Punctuation Accurately:
    +	Detailed explanation: The essay generally maintains a high level of grammatical accuracy with few errors. There are a few minor issues such as subject-verb agreement ("activities have been devastating") and article usage ("in the balance of the ecosystem"). Punctuation is appropriately used to clarify meaning and structure sentences effectively. For instance, commas are used correctly to set off introductory phrases and separate items in a series.
    +	How to improve: To improve grammatical accuracy further, pay closer attention to subject-verb agreement throughout the essay. Ensure that articles ('a', 'the') are used appropriately before singular nouns. Review the use of prepositions to ensure precise expression ('in not only the balance of the ecosystem but also in our lives'). Consider revising sentences for clarity and conciseness, avoiding any potential ambiguity caused by complex structures or word choice.
**Overall**
Overall Score: 7.25
Overall, this essay exhibits a strong command of grammatical structures and punctuation, contributing to its coherence and clarity. Continued focus on incorporating a wider variety of sentence structures and refining grammatical accuracy will further enhance the overall quality of writing.
"""

essay_prompt_2 = """
## Input :
**Topic**
The increase in the production of consumer goods results in damage to the natural environment. What are the causes of this? What can be done to solve this problem?
**Assignment**
Nowadays , as more consumer goods are manufactured, more damage has been inflicted on the environment. I will outline  several reasons for this and put forward some measures to this issue.
First of all , the increase in the production of consumer products harms the environment in two ways: the chemical by-products from the manufacturing process and the mass production of disposable goods. As more goods are produced, more toxic wastes and emissions are released from factories into nature. water sources are contaminated , and the air is severely polluted , which results in the deaths of many marine and terrestrial animals . Also, to accommodate customers’ ever-increasing demands , more single-use products are introduced, most of which are  non-biodegradable . Though having a short lifespan, these products can remain as wastes  for thousands of years, turning our planet into a huge landfill  and posing a threat to the living habitats of all creatures.
Actions must be taken as soon as possible  to minimize the negative impacts on the environment arising from the increasing amount of consumer goods. First, companies should promote the use of eco-friendlier  materials. For example , the giant coffee chain Starbucks  has recently replaced  plastic straws with reusable alternatives made of materials like paper or bamboo. in addition , many governments are also encouraging the development of more sustainable manufacturing processes. For instance, many states in the U.S  offer tax breaks and incentives for businesses using renewable energy, and some firms are even allowed to purchase green energy at cheaper prices than traditional fossil fuels.
In conclusion, there are two main reasons why the environment is severely impacted by the increase in the production of consumer goods. To address this issue, governments and companies must join hands  to make the production lines more environmentally friendly by switching to greener materials.

## Feedback :
**Vocabulary and Grammar Enhancement**
-   Nowadays-> In contemporary times
Explanation: "Nowadays" is colloquial and less formal compared to "In contemporary times," which is more suitable for academic writing.
-	I will outline-> This essay outlines
Explanation: Using "I will outline" is unnecessary as it introduces a personal tone. Changing it to "This essay outlines" maintains a formal tone appropriate for academic writing.
-	First of all-> Primarily
Explanation: "First of all" is too informal for academic writing. "Primarily" is a more formal and appropriate transition to introduce the first point.
-	hurts the environment-> harms the environment
Explanation: "Hurts" is overly simplistic and lacks precision. "Harms" is a more accurate and formal term commonly used in academic contexts.
-	water sources are contaminated-> water sources become contaminated
Explanation: The change to "become contaminated" provides a more active voice, which is preferred in academic writing, and it maintains the formal tone.
-	and the air is severely polluted-> resulting in severe air pollution
Explanation: Restructuring the sentence to "resulting in severe air pollution" makes it more concise and aligns with academic style by avoiding unnecessary repetition.
-	which results in the deaths of many marine and terrestrial animals-> leading to the mortality of numerous marine and terrestrial animals
Explanation: "Results in the deaths" can be refined to "leading to the mortality" for a more formal tone and precise language commonly found in academic writing.
-	to accommodate customers’ ever-increasing demands-> to meet the escalating demands of consumers
Explanation: "Accommodate customers’ ever-increasing demands" is slightly informal. "Meet the escalating demands of consumers" is more formal and better suited to academic writing.
-	introduced, most of which are-> introduced, the majority of which are
Explanation: Adding "the majority of which are" enhances clarity and formality by specifying the proportion of single-use products that are non-biodegradable.
-	non-biodegradable-> non-biodegradable ones
Explanation: Adding "ones" provides clarity and grammatical completeness, which is preferred in formal writing.
-	as wastes-> as waste
Explanation: "As wastes" is grammatically incorrect. "As waste" is the correct usage in this context.
-	turning our planet into a huge landfill-> transforming our planet into an enormous landfill
Explanation: "Turning" can be replaced with "transforming" for a more formal tone. "Enormous" is also more precise than "huge" in academic writing.Actions must be taken as soon as possible-> Immediate action must be taken
Explanation: The phrase "as soon as possible" is informal. Replacing it with "Immediate action must be taken" maintains formality and conciseness.
-	eco-friendlier-> more environmentally friendly
Explanation: "Eco-friendlier" is informal. "More environmentally friendly" is a more precise and formal term suitable for academic writing.
-	For example-> For instance
Explanation: "For example" is slightly informal. "For instance" is a more formal alternative commonly used in academic writing.
-	the giant coffee chain Starbucks-> the renowned coffee chain Starbucks
Explanation: "Giant" is too informal. "Renowned" adds a formal and descriptive touch appropriate for academic writing.
-	recently replaced-> recently substituted
Explanation: "Replaced" is overly simplistic. "Substituted" is a more formal synonym suitable for academic writing.
-	in addition-> Furthermore
Explanation: "In addition" is slightly informal. "Furthermore" is a more formal transition commonly used in academic writing.
-	many states in the U.S-> numerous states in the United States
Explanation: "Many states in the U.S" lacks formality and specificity. "Numerous states in the United States" is more precise and formal.
-	join hands-> collaborate
Explanation: "Join hands" is idiomatic and informal. "Collaborate" is a more formal alternative suitable for academic writing.

**Strengthening the Argument**
-   Introduction: "Nowadays, as more consumer goods are manufactured, more damage has been inflicted on the environment. I will outline several reasons for this and put forward some measures to this issue.
    +	Explanation: The introduction clearly states the topic and purpose of the essay, setting the stage for the discussion to follow.
    +	Improved Example: "The relentless increase in the production of consumer goods has led to significant environmental degradation. This essay will examine the underlying causes of this problem and propose practical solutions to mitigate its negative impacts on our planet."
-	Main Point 1: "As more goods are produced, more toxic wastes and emissions are released from factories into nature. Water sources are contaminated, and the air is severely polluted, which results in the deaths of many marine and terrestrial animals.
    +	Explanation: This point effectively explains the environmental impact of toxic wastes and emissions, emphasizing the harm to marine and terrestrial life.
    +	Improved Example: "The excessive production of consumer goods leads to the release of hazardous chemicals into waterways and the atmosphere. These chemicals contaminate water sources, making them unsafe for aquatic life, including fish, birds, and mammals. Additionally, air pollution from factories and transportation associated with consumer goods production harms terrestrial ecosystems, disrupting the balance of ecosystems and threatening the survival of many species."
-	Main Point 2: "Also, to accommodate customers’ ever-increasing demands, more single-use products are introduced, most of which are non-biodegradable. Though having a short lifespan, these products can remain as wastes for thousands of years, turning our planet into a huge landfill and posing a threat to the living habitats of all creatures.
    +	Explanation: This point highlights the problem of non-biodegradable single-use products, emphasizing their long-term environmental impact.
    +	Improved Example: "The proliferation of single-use products, such as plastic bags, straws, and packaging, has contributed significantly to the waste crisis. These items are not biodegradable, meaning they can remain in landfills for centuries, accumulating and polluting the environment. This waste threatens the habitats of wildlife, clogs waterways, and contributes to climate change."
-	Main Point 3: "First, companies should promote the use of eco-friendlier materials. For example, the giant coffee chain Starbucks has recently replaced plastic straws with reusable alternatives made of materials like paper or bamboo.
    +	Explanation: This point suggests a solution by promoting eco-friendly materials, using the example of Starbucks' switch to reusable straws.
    +	Improved Example: "Companies can play a crucial role in reducing environmental harm by adopting eco-friendly materials in their production processes. For instance, Starbucks' decision to replace plastic straws with reusable alternatives made of sustainable materials demonstrates a positive shift towards environmental responsibility."
-   Main Point 4 : "In addition, many governments are also encouraging the development of more sustainable manufacturing processes. For instance, many states in the U.S offer tax breaks and incentives for businesses using renewable energy, and some firms are even allowed to purchase green energy at cheaper prices than traditional fossil fuels.
    +   Explanation: This point highlights government initiatives to promote sustainable manufacturing processes, using the example of tax breaks and incentives for businesses using renewable energy.
    +   Improved Example: "Governments can also support the transition to sustainable manufacturing by offering tax incentives and subsidies to businesses that adopt eco-friendly practices. This encourages companies to invest in renewable energy sources, reduce waste, and adopt more sustainable production methods, ultimately reducing their environmental footprint."
-	Conclusion: "In conclusion, there are two main reasons why the environment is severely impacted by the increase in the production of consumer goods. To address this issue, governments and companies must join hands to make the production lines more environmentally friendly by switching to greener materials.
    +	Explanation: The conclusion effectively summarizes the main points and reiterates the need for collaboration between governments and companies to address the problem.
    +	Improved Example: "In conclusion, the increase in consumer goods production has led to significant environmental damage through the release of toxic chemicals, the mass production of disposable goods, and the accumulation of waste. To mitigate these negative impacts, it is imperative that governments and companies work together to promote eco-friendly materials, encourage sustainable manufacturing practices, and implement policies that incentivize environmentally responsible behavior."
Overall, the essay provides a well-structured and informative discussion of the causes and solutions to the environmental damage caused by the increase in consumer goods production. By incorporating specific examples and elaborating on the interconnectedness of these factors, the argument can be further strengthened and made more persuasive.
**Task Response**
Band Score for Task Response: 8
-	Answer All Parts of the Question:
    +   Detailed explanation: The essay effectively addresses all components of the prompt. It discusses both the causes of environmental damage resulting from increased production of consumer goods and proposes solutions to mitigate this problem.
    +	How to improve: While the essay adequately covers all aspects of the prompt, a deeper exploration of the consequences of environmental damage or potential long-term implications could enrich the analysis.
-	Present a Clear Position Throughout:
    +	Detailed explanation: The essay maintains a clear position throughout, acknowledging the detrimental effects of increased consumer goods production on the environment and advocating for proactive measures to address this issue.
    +	How to improve: To enhance clarity further, consider explicitly stating the writer's stance in the introduction and reiterating it in the conclusion for emphasis.
-	Present, Extend, and Support Ideas:
    +	Detailed explanation: The essay presents ideas logically, supporting them with relevant examples such as the adverse effects of chemical by-products and disposable goods on the environment. However, it could benefit from further elaboration and deeper analysis of these examples.
    +	How to improve: To extend ideas, provide more detailed explanations or additional examples to bolster arguments and provide a more comprehensive understanding of the topic.
-	Stay on Topic:
    +	Detailed explanation: The essay remains focused on the topic throughout, discussing reasons why it is essential for humans to prevent animal species from becoming extinct. It does not deviate into tangential discussions.
    +	How to improve: To ensure continued relevance, maintain a clear connection between each point and the central theme, avoiding tangential discussions that may detract from the main argument.
Overall, this essay demonstrates a strong understanding of the prompt and effectively addresses the key components of the task. To improve further, the writer could deepen their analysis, provide more extensive support for arguments, and enhance clarity by explicitly stating their position and maintaining a strong focus on the topic throughout the essay.
**Coherence & Cohesion**
Band Score for Coherence and Cohesion: 7
-	Organize Information Logically:
    +	Detailed explanation: The essay demonstrates a clear logical organization throughout. It begins with an introduction that outlines the main points to be discussed: the causes of environmental damage due to increased consumer goods production and potential solutions. Each body paragraph then explores one cause or solution in depth, offering clear explanations and examples to support the points. Finally, the conclusion succinctly summarizes the main arguments presented in the essay. The logical flow from introduction to body paragraphs to conclusion enhances the overall coherence of the essay
    +	How to improve: While the logical organization is generally strong, a minor improvement could be made in the introduction by providing a more specific thesis statement that directly addresses the essay prompt. Additionally, ensuring smooth transitions between paragraphs can further enhance coherence.
-	Use Paragraphs:
    +	Detailed explanation: The essay effectively utilizes paragraphs to structure its content. Each paragraph addresses a specific aspect of the argument, such as the causes of extinction and the importance of preserving wildlife. The opening and closing paragraphs appropriately introduce and conclude the essay, respectively.
    +	How to improve: To further improve paragraphing, ensure that each paragraph maintains a clear focus on its central idea and provides sufficient elaboration. Consider varying sentence structures within paragraphs to enhance readability and engagement.
-	Use a Range of Cohesive Devices:
    +	Detailed explanation: The essay effectively utilizes a range of cohesive devices to connect ideas and enhance coherence. Examples include cohesive devices such as transition words ("First of all," "In addition," "In conclusion"), pronouns ("this issue"), and repetition of key terms ("environment," "consumer goods"). These cohesive devices help to signal relationships between ideas, making the essay easier to follow and reinforcing the overall coherence.
    +	How to improve: While the essay already incorporates cohesive devices well, further diversifying the types of cohesive devices used can add richness to the essay's coherence. Consider incorporating cohesive devices such as synonyms, parallel structure, and referencing previous points to further strengthen the connections between ideas. Additionally, ensuring that cohesive devices are used consistently and appropriately throughout the essay can enhance overall cohesion.
**Lexical Resource**
Band Score for Lexical Resource: 7
-	Use a Wide Range of Vocabulary:
    +	Detailed explanation: The essay demonstrates a commendable range of vocabulary relevant to the topic of environmental damage caused by the production of consumer goods. Phrases such as "chemical by-products," "mass production," "disposable goods," "toxic wastes," "biodegradable," and "renewable energy" contribute to a nuanced discussion of the issue.
    +	How to improve: To further enhance lexical variety, consider incorporating more specialized terms related to environmental science and sustainable practices. For instance, instead of repeating phrases like "consumer goods" or "environment," use synonyms or specific terms like "consumer products" or "ecosystem" to avoid redundancy and add depth to the analysis.
-	Use Vocabulary Precisely:
    +	Detailed explanation: The essay generally employs vocabulary with precision, effectively conveying ideas related to environmental degradation caused by consumerism. For example, the distinction between "chemical by-products" and "mass production of disposable goods" highlights a clear understanding of the various aspects contributing to environmental harm.
    +	How to improve: While the essay demonstrates precise vocabulary usage overall, ensure consistency in terminology throughout the essay. Avoid vague or overly general terms that may detract from the clarity of your arguments. Additionally, strive to incorporate domain-specific terminology accurately to strengthen the essay's credibility and depth.
-	Use Correct Spelling:
    +	Detailed explanation: Spelling accuracy is generally maintained throughout the essay, contributing to its overall coherence and professionalism. Common words and phrases are spelled correctly, enhancing readability and comprehension for the reader.
    +	How to improve: To further improve spelling accuracy, consider utilizing spell-checking tools or proofreading techniques to identify and correct any potential errors. Additionally, expanding your vocabulary and familiarity with word patterns can help reduce spelling mistakes and enhance overall writing fluency.
Overall, the essay demonstrates a strong command of vocabulary, with precise usage and generally accurate spelling contributing to its effectiveness in addressing the prompt. To further elevate the lexical resource, continue expanding your vocabulary repertoire, strive for consistency in terminology, and maintain a keen focus on spelling accuracy to ensure clarity and coherence in your writing.
**Grammatical Range & Accuracy**
Band Score for Grammatical Range and Accuracy: 7
-	Use a Wide Range of Structures:
    +	Detailed explanation: The essay demonstrates a commendable variety of sentence structures. It utilizes simple, compound, and complex sentences effectively throughout the text. For instance, it starts with a complex sentence to introduce the topic: "Nowadays, as more consumer goods are manufactured, more damage has been inflicted on the environment." The essay also incorporates compound sentences to present arguments and supporting details, such as: "As more goods are produced, more toxic wastes and emissions are released from factories into nature." Furthermore, it utilizes parallel structures for emphasis, as seen in the sentence: "Water sources are contaminated, and the air is severely polluted, which results in the deaths of many marine and terrestrial animals."
    +	How to improve: While the essay displays a good range of sentence structures, further variation can enhance readability and engagement. Introducing rhetorical questions, occasional exclamatory sentences, or incorporating inverted sentences for emphasis can add depth to the prose and maintain the reader's interest.
-	Use Grammar and Punctuation Accurately:
    +	Detailed explanation: Overall, the essay demonstrates a strong command of grammar and punctuation. Sentences are structured correctly, and punctuation marks are used appropriately to clarify meaning and enhance readability. For example, the essay employs commas effectively to separate items in a list ("Water sources are contaminated, and the air is severely polluted...") and to set off introductory phrases ("First of all, the increase in the production of consumer products harms the environment in two ways:..."). Moreover, the essay maintains subject-verb agreement and uses articles, prepositions, and conjunctions accurately.
    +	How to improve: While the essay's grammar and punctuation are largely accurate, some minor errors are present. Proofreading for consistency in verb tense usage and ensuring parallelism in structures can further refine the essay's clarity and cohesion. Additionally, paying attention to sentence fragments and run-on sentences can enhance the overall fluency of the writing.
**Overall**
Overall score : 7.25
Overall, the essay demonstrates strong proficiency in grammatical range and accuracy, contributing to its effective communication of ideas. By incorporating a wider variety of sentence structures and maintaining precise grammar and punctuation usage, the essay can further elevate its coherence and sophistication, potentially leading to an even higher band score.
"""

def get_writing_result(topic, assignment):
    prompt_part = [
    """
You are a highly skilled IELTS instructor, tasked with effectively correcting IELTS Writing Task 2 submissions.
Your responses should be clear and easily understandable for students who are learning English.

    """,
f"""Please follow the instructions below and you must use the form provided:
    {essay_prompt_1}
    """,
f"""Please follow the instructions below and you must use the form provided:
    {essay_prompt_2}
    """,
    f"""
## Input :
**Topic: {topic}
**Assignment: {assignment}
## Feedback :
    """
]
    prompt = ''.join(prompt_part)
    # Use the generative model to generate the content
    model = genai.GenerativeModel('gemini-1.5-pro-latest',generation_config=generation_config,safety_settings=safety_settings)
    response = model.generate_content(prompt, request_options={"timeout" : 200})
        

    return response.text