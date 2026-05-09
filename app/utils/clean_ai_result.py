import json
import re

def clean_ai_result(ai_result):

    raw = ai_result.get("match_score")

    if not raw:
        return ai_result

    if isinstance(raw, str):

        # remove markdown
        cleaned = re.sub(r"```json|```", "", raw).strip()

        try:
            parsed = json.loads(cleaned)

            ai_result["score"] = parsed.get("score") or parsed.get("match_percentage") or 0
            ai_result["recommendation"] = parsed.get("recommendation")
            ai_result["missing_skills"] = parsed.get("missing_skills") or parsed.get("skill_gaps", [])
            ai_result["matched_skills"] = parsed.get("matched_skills", [])
            ai_result["strengths"] = parsed.get("strengths", [])
            ai_result["weaknesses"] = parsed.get("weaknesses", [])

        except Exception as e:
            logger.error(f"Failed parsing match_score: {e}")

    return ai_result