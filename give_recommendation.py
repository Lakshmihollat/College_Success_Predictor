# give_recommendation.py

def give_recommendation(attendance, activity_level, math, reading, writing):
    recs = []
    avg_score = (math + reading + writing) / 3

    if attendance < 85:
        recs.append("📌 Try to maintain attendance above 85% for better consistency.")
    if activity_level < 3:
        recs.append("📌 Participate in more academic or co-curricular activities.")
    if avg_score < 70:
        recs.append("📌 Focus more on exam preparation – average score is low.")
    if attendance >= 90 and avg_score >= 80:
        recs.append("✅ You’re doing great! Keep up the excellent work.")
    
    return recs
