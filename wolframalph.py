import wolframalpha

wolframalpha_API_ID = '5UQVG8-L5HU8645K8'

def wolframalphafunc(query):
    try:
        client = wolframalpha.Client(wolframalpha_API_ID)

        # Stores the response from
        # wolf ram alpha
        res = client.query(query)

        # Includes only text from the response
        answer = next(res.results).text

        return answer

    except Exception as e :
        return "We tried your query on wolframaplha... \n" \
               "But we couldn't find anything...."

