def calculator(a, b):
    return a + b


def agent(user_input):

    if "add" in user_input.lower():
        print("Agent: I should use the calculator tool.")

        result = calculator(10, 20)

        print("Tool result:", result)

        return f"The answer is {result}"

    return "I don't know how to handle that request."


question = input("You: ")

answer = agent(question)

print("Agent:", answer)