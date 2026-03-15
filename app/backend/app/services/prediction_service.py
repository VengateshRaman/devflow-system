# from app.ml.inference import predict_price

# class PredictionService:

#     @staticmethod
#     def predict(area: int, bedrooms: int):
#         price = predict_price(area, bedrooms)

#         return {
#             "predicted_price": price
#         }


from app.ml.inference import predict_price

class PredictionService:

    def predict(self, area: int, bedrooms: int):

        price = predict_price(area, bedrooms)

        return {
            "predicted_price": price
        }