from playwright.sync_api import Playwright

orders_payload = {
    "orders": [{"country": "India",
                "productOrderedId": "6960eac0c941646b7a8b3e68"}
              ]
}
class ApiUtils:

    def get_token(self,playwright: Playwright,user_credentials:dict):
        ctx = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = ctx.post("/api/ecom/auth/login", data={"userEmail":user_credentials["email"],"userPassword":user_credentials["password"]})

        assert response.ok
        token = response.json()["token"]
        return token

    def create_order(self,playwright: Playwright,user_credentials:dict):
        token = self.get_token(playwright,user_credentials)
        ctx =playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = ctx.post("api/ecom/order/create-order",data=orders_payload,headers={"Authorization":token,"Content-Type":"application/json"} )
        assert response.ok
        print(f"Status: {response.status}")
        print(f"Response: {response.json()}")
        order_id = response.json()["orders"][0]
        print(f"order_id:{order_id}")
        return order_id