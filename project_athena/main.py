from modules.retriever import retrieve_data
from modules.reasoner_mistral import reason_over_data

def run():
    content = retrieve_data()
    summary = reason_over_data(content)
    print("\n�� Agent Summary:\n", summary)

if __name__ == "__main__":
    run()
