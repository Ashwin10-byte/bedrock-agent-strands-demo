import boto3

KNOWLEDGE_BASE_ID = "W1RZOXOKMI"
REGION_NAME = "us-east-1"
MODEL_ARN = f"arn:aws:bedrock:{REGION_NAME}::foundation-model/amazon.nova-lite-v1:0"

def query_knowledge_base(question):
    bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name=REGION_NAME)

    print("Querying Bedrock Knowledge Base...")
    print("=" * 60)
    print(f"Knowledge Base ID : {KNOWLEDGE_BASE_ID}")
    print(f"Question          : {question}\n")

    try:
        response = bedrock_agent_runtime.retrieve_and_generate(
            input={'text': question},
            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': KNOWLEDGE_BASE_ID,
                    'modelArn': MODEL_ARN
                }
            }
        )

        output_text = response['output']['text']
        print("Answer:")
        print(output_text)
        print("\n" + "-" * 60)

        citations = response.get('citations', [])
        if citations:
            print("\nSources:")
            for idx, citation in enumerate(citations, 1):
                for reference in citation.get('retrievedReferences', []):
                    uri = reference.get('location', {}).get('s3Location', {}).get('uri', 'Unknown')
                    print(f"  [{idx}] {uri}")

    except Exception as e:
        print(f"\nError querying Knowledge Base: {e}")

if __name__ == "__main__":
    query_knowledge_base("When is spring break this year?")
