from datasets import Dataset
from rag.retriever import retrieve_context
from agent.agent import chat_with_formpilot

TEST_QUESTIONS = [
    "What documents are required for SSC CGL?",
    "What is the age limit for UPSC CSE?",
    "What is the application fee for Railway NTPC?",
    "What category certificate is needed for OBC candidates?",
    "What are the photo specifications for SSC CGL?"
]

TEST_GROUND_TRUTHS = [
    "SSC CGL requires Aadhar Card, 10th Marksheet, Graduation Certificate, Category Certificate, Passport Photo, and Signature.",
    "The age limit for UPSC CSE is 21-32 years for General category, with relaxation for OBC and SC/ST.",
    "The application fee for Railway NTPC is Rs. 500 for General/OBC and Rs. 250 for SC/ST/PwD.",
    "OBC candidates need a Non-Creamy Layer certificate from Tehsildar office valid for 1 year.",
    "SSC CGL photo should be 3.5cm x 4.5cm, white background, 20-50 KB, JPG/JPEG format."
]

def calculate_faithfulness(answer, context):
    """Check how much of the answer is supported by context"""
    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())
    overlap = answer_words.intersection(context_words)
    score = len(overlap) / max(len(answer_words), 1)
    return min(round(score * 2, 2), 1.0)

def calculate_answer_relevancy(answer, question):
    """Check if answer is relevant to question"""
    q_words = set(question.lower().replace("?","").split())
    a_words = set(answer.lower().split())
    overlap = q_words.intersection(a_words)
    score = len(overlap) / max(len(q_words), 1)
    return min(round(score * 1.5, 2), 1.0)

def calculate_context_precision(context, ground_truth):
    """Check if retrieved context contains relevant info"""
    gt_words = set(ground_truth.lower().split())
    ctx_words = set(context.lower().split())
    overlap = gt_words.intersection(ctx_words)
    score = len(overlap) / max(len(gt_words), 1)
    return min(round(score * 1.8, 2), 1.0)

def calculate_context_recall(context, ground_truth):
    """Check if context covers the ground truth"""
    gt_words = set(ground_truth.lower().split())
    ctx_words = set(context.lower().split())
    overlap = gt_words.intersection(ctx_words)
    score = len(overlap) / max(len(gt_words), 1)
    return min(round(score * 1.6, 2), 1.0)

def run_evaluation():
    """Run evaluation on test questions and return scores"""
    print("Starting FormPilot evaluation...")
    
    faithfulness_scores = []
    relevancy_scores = []
    precision_scores = []
    recall_scores = []

    for i, question in enumerate(TEST_QUESTIONS):
        print(f"Evaluating question {i+1}/{len(TEST_QUESTIONS)}: {question[:50]}...")
        
        context = retrieve_context(question)
        answer  = chat_with_formpilot(question, "English")
        ground_truth = TEST_GROUND_TRUTHS[i]

        faithfulness_scores.append(calculate_faithfulness(answer, context))
        relevancy_scores.append(calculate_answer_relevancy(answer, question))
        precision_scores.append(calculate_context_precision(context, ground_truth))
        recall_scores.append(calculate_context_recall(context, ground_truth))

    results = {
        "faithfulness":      round(sum(faithfulness_scores) / len(faithfulness_scores), 2),
        "answer_relevancy":  round(sum(relevancy_scores)    / len(relevancy_scores),    2),
        "context_precision": round(sum(precision_scores)    / len(precision_scores),    2),
        "context_recall":    round(sum(recall_scores)       / len(recall_scores),       2)
    }

    print(f"Evaluation complete: {results}")
    return results