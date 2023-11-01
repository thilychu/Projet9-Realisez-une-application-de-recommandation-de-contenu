import azure.functions as func
import logging
import pandas as pd
import joblib


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    user_id = req.params.get('userId')
    print(user_id)
    if not user_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            user_id = req_body.get('userId')

    if user_id: 
        model = joblib.load('./WebAppHttpTrigger/svd_model.pkl')
        articles_ids = pd.read_csv("./WebAppHttpTrigger/articles_ids.csv",sep=";")
        closest_article_ids = get_collaborative_reco(user_id, model, articles_ids)
        return func.HttpResponse(f"{closest_article_ids}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


def get_collaborative_reco(user_id, model, articles_df, n=5):
    # Predict ratings for all articles for the given user

    predictions = []
    for article_id in articles_df["article_id"]:
        try:
            predictions.append(model.predict(uid=user_id, iid=int(article_id)))
        except Exception as e:
            # Log the exception for debugging
            print(f"Error processing article_id {article_id}: {str(e)}")


    # Create a DataFrame from the predictions
    prediction_df = pd.DataFrame(predictions, columns=["uid", "iid", "rating", "est", "details"])

    # Sort the DataFrame by predicted rating in descending order
    sorted_df = prediction_df.sort_values(by="est", ascending=False)

    # Get the top N article IDs
    top_n_article_ids = sorted_df["iid"].head(n).tolist()

    return top_n_article_ids
