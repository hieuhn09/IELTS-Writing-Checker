import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyBk2M6CBT8YlWsBPKs4UGlHm35fE_tBB8s'

topic = (
    "Some people think that parents should teach their children how to be good members of society. "
    "Others, however, believe that school is the best place to learn this. "
    "Discuss both views and give your own opinion."
)
assignment = (
    "Some people believe that children should be taught by their parents about how to function as useful members of society, "
    "while others believe that sending children to educational institutions is the best way for them to study this. "
    "Although the latter opinion can be beneficial in some cases, I believe that family upbringing plays a more important role in educating children to be good parts of the community.\n\n"
    
    "Schools can be considered suitable places for children to learn to be good citizens. "
    "With standardized educational methods, schools can foster children’s cognitive development so that they are able to contribute to society in the future. "
    "For example, Trung Vuong school and Vinschool are well known for having nurtured successful alumni such as Professor Ngo Bao, Professor Nguyen Hung who have devoted their talents to the development of the country. "
    "However, these people only represent a small fraction of the total number of students attending schools, and thus sending children to schools cannot be the best method of educating them to be good members of society.\n\n"

    "I believe that parents play a more important role in teaching them how to be good citizens. "
    "In Vietnam, the average class size is 20 students, which makes it difficult for educators to provide proper schooling for each student. "
    "One to one lessons at home, on the other hand, allow children to progress faster. "
    "Furthermore, parents form stronger bonds with their offspring and thus, it is easier for them to shape children’s personalities at an early age. "
    "For example, by telling stories such as Robin Hood, Cinderella before bedtime, parents can instil a sense of compassion and integrity into them. "
    "These children are likely to become good members of society when they grow up.\n\n"

    "In conclusion, although sending children to schools can be seen as a way of teaching them how to be good citizens, "
    "I believe that domestic upbringing has a bigger impact on determining who they are in the future."
)
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(f"I have a IELTS writing task and you are the teacher, who grade and comments on my work\n"\
                                  f"Topic : {topic}\n"\
                                  f"Assignment : {assignment}\n"\
                                  )
print(response.text)