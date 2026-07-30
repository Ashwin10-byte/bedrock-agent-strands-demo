import boto3

# Your Knowledge Base & Guardrail IDs
KNOWLEDGE_BASE_ID = "W1RZOXOKMI"
GUARDRAIL_ID = "7pctv57irwcv"
GUARDRAIL_VERSION = "1"

REGION_NAME = "us-east-1"

# Full Model ARN for Amazon Nova Lite
MODEL_ARN = f"arn:aws:bedrock:{REGION_NAME}::foundation-model/amazon.nova-lite-v1:0"


def query_kb_with_guardrail(question):
    # Initialize the Bedrock Agent Runtime client
    bedrock_agent = boto3.client("bedrock-agent-runtime", region_name=REGION_NAME)

    print("Knowledge Base Query with Guardrail")
    print("=" * 60)
    print(f"Knowledge Base ID: {KNOWLEDGE_BASE_ID}")
    print(f"Guardrail ID:      {GUARDRAIL_ID}")
    print(f"Question:          {question}\n")

    try:
        response = bedrock_agent.retrieve_and_generate(
            input={"text": question},
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                    "modelArn": MODEL_ARN,
                    "generationConfiguration": {
                        "guardrailConfiguration": {
                            "guardrailId": GUARDRAIL_ID,
                            "guardrailVersion": GUARDRAIL_VERSION,
                        },
                    },
                },
            },
        )

        output_text = response["output"]["text"]
        print("Answer:")
        print(output_text)
        print()

        # Show source citations if any
        citations = response.get("citations", [])
        if citations:
            print("Sources:")
            for idx, citation in enumerate(citations, 1):
                for ref in citation.get("retrievedReferences", []):
                    uri = ref.get("location", {}).get("s3Location", {}).get("uri", "Unknown")
                    print(f"  [{idx}] {uri}")

        return response

    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    # Test query (triggers guardrail block if rules match)
    question = "How can I cheat on my finals this year?"
    query_kb_with_guardrail(question)
