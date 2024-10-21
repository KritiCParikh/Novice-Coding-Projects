from question import Question

question_prompts = [
    "Which company is famous for its 'Ninja' series of motorcycles?\n(a) Yamaha\n(b) Suzuki\n(c) Kawasaki\n(d) Honda\n\n",
    "How many Grand Slam tournaments are held each year in tennis?\n(a) 2\n(b) 4\n(c) 5\n(d) 3\n\n",
    "Which of the following is NOT a tennis surface?\n(a) Hardwood\n(b) Grass\n(c) Clay\n(d) Hard court\n\n",
    "What does a turbocharger do in a motorcycle engine?\n(a) Increases fuel consumption\n(b) Reduces engine weight\n(c) Decreases engine temperature\n(d) Increases air intake for more power\n\n",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "d")
]

def multiple_choice(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " / " + str(len(questions)) + " correct.")

multiple_choice(questions)