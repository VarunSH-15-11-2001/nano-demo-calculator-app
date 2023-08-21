#include "crow_all.h"
#include <iostream>
using namespace std;

crow::response greet()
{
    return crow::response{"Hello World!"};
}
crow::response add(const crow::request& req)
{
    auto input = crow::json::load(req.body);

    int firstValue = input["first"].i();
    int secondValue = input["second"].i();

    int result = firstValue + secondValue;

    return crow::response { "{\"result\":" + to_string(result) + "}" };
}
crow::response add(const crow::request& req)
{
    auto input = crow::json::load(req.body);

    int firstValue = input["first"].i();
    int secondValue = input["second"].i();

    int result = firstValue - secondValue;

    return crow::response { "{\"result\":" + to_string(result) + "}" };
}