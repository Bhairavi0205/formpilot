from langchain.tools import tool
from rag.retriever import retrieve_context
from utils.deadline import get_upcoming_deadlines
from utils.photo_resize import resize_image_for_exam

@tool
def search_exam_info(query: str) -> str:
    """Search for exam information, eligibility, documents, fees from knowledge base"""
    context = retrieve_context(query)
    if not context:
        return "Is exam ke baare mein mujhe jaankari nahi mili. Please official website check karo."
    return context

@tool
def get_deadlines(exam_name: str) -> str:
    """Get upcoming deadlines for a specific exam"""
    deadlines = get_upcoming_deadlines(exam_name)
    return deadlines

@tool
def validate_form_details(details: str) -> str:
    """Validate user's form details before submission"""
    issues = []
    details_lower = details.lower()
    
    if "name" in details_lower:
        issues.append("✓ Name — 10th marksheet se exactly match karna chahiye")
    if "dob" in details_lower or "date of birth" in details_lower:
        issues.append("✓ DOB — DD/MM/YYYY format mein hona chahiye")
    if "photo" in details_lower:
        issues.append("✓ Photo — White background, correct size, recent honi chahiye")
    if "category" in details_lower:
        issues.append("✓ Category — Certificate se match karna chahiye")
    
    if not issues:
        return """Form details check karo:
- Name: 10th marksheet se exactly match kare
- DOB: DD/MM/YYYY format
- Category: Certificate se match kare  
- Photo: White background, correct KB size
- Mobile/Email: Active aur correct hai"""
    
    return "Form Validation Checklist:\n" + "\n".join(issues)