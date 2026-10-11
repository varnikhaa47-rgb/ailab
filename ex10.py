# AI-Based Course Recommendation System Using Python
courses = { "Python for AI": ["python", "programming"], "Machine Learning": ["python", "machine learning", "statistics"], "Deep Learning": ["python", "deep learning", "neural networks"], "Data Science": ["python", "statistics", "data analysis"], "Natural Language Processing": ["python", "nlp", "machine learning"] }

print("AI COURSE RECOMMENDATION SYSTEM") 
print("--------------------------------") 

skills = input("Enter your skills (comma separated): ").lower().split(",") 
skills = [skill.strip() for skill in skills]

recommendations = []
 
for course, required_skills in courses.items(): 
score = 0 
for skill in skills: 
if skill in required_skills: 
score += 1 
recommendations.append((course, score)) 

recommendations.sort(key=lambda x: x[1], reverse=True)
 
print("\nRecommended Courses:") 
print("--------------------") 

for course, score in recommendations[:3]: 
print(course, "- Match Score:", score) 

print("\nRecommendation completed successfully!") 