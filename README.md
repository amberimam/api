## REST API

This is a proposed implementation for a REST API to support Gemnote's web application at www.gemnote.com. It supports getting a list of products (filterable by category), and getting a specific product by product ID. It is written in python and uses flask and webargs libraries.

### Contents
```
.
├── README.md
├── api.py
├── db.json
└── requirements.txt
```

#### api.py
This is the file which implements the REST API. All of the logic to support the api is contained in this file.

#### db.json
This file contains detailed information about four products offered for sale at Gemnote, in json format.

#### requirements.txt
This file lists python dependencies for the api.

### Installation
* Install **python3** or **python2** if it is not installed on your system already. http://docs.python-guide.org/en/latest/starting/installation/
* Install **pip** if its not present already. https://pip.pypa.io/en/stable/installing/
* Download the contents of this repository into a directory named `api`.
* Execute the following command in the `api` directory: `pip install -r requirements.txt`

### Running the program
Execute the following command in the `api` directory: `python api.py`.
You should see output similar to this if it is running successfully:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 974-957-933
```

### REST APIs:

#### Get a list of all products. 

Optional filtering by category. Multiple categories are ANDed together.

**GET /products?category=:category1&category=:category2**

Example Request and Response:

Request: `GET http://127.0.0.1:5000/products?category=Apparel&category=Women`

Success Response: code 200 and content:

```json
[
    {
        "name": "Patagonia Hybrid Jacket",
        "categories": [
            "Apparel",
            "Women"
        ],
        "types": [
            {
                "color": "black",
                "image_url": "https://gemnote-images-production.s3-us-west-2.amazonaws.com/images/images/000/000/899/full_size/patagonia_women_s_adze_hybrid_jacket___black.jpg?1510663389"
            },
            {
                "color": "white",
                "image_url": "https://gemnote-images-production.s3-us-west-2.amazonaws.com/images/images/000/000/899/full_size/patagonia_women_s_adze_hybrid_jacket___black.jpg?1510663389"
            }
        ],
        "description": [
            "93% polyester/7% spandex stretch woven with fleece grid backer",
            "3-layer Polartec Windbloc stretch-woven polyester soft-shell with a DWR (durable water repellent) finish",
            "Stretchy, breathable, double-weave soft-shell fabric on side panels, underarms and cuffs",
            "High, harness- and pack-compatible handwarmer pockets and one interior chest pocket have brushed tricot lining"
        ],
        "price": {
            "amount": 189,
            "currency": "USD",
            "num_units": 1
        },
        "id": 2
    }
]
```

#### Get details of one product by id
**GET /products/:id**

Example Request and Response:

Request: `GET http://127.0.0.1:5000/products/1`

Success Response: code 200 and content:

```json
{
    "name": "Kinto Ceramic Lab Tall Mug",
    "categories": [
        "Drinkware"
    ],
    "types": [
        {
            "color": "Beige",
            "image_url": "https://gemnote-images-production.s3-us-west-2.amazonaws.com/images/images/000/001/528/full_size/kinto_ceramic_lab_tall_mug___beige.jpg?1510664122"
        },
        {
            "color": "Black",
            "image_url": "https://gemnote-images-production.s3-us-west-2.amazonaws.com/images/images/000/001/276/full_size/kinto_ceramic_lab_tall_mug___black.jpg?1510664124"
        },
        {
            "color": "Brown",
            "image_url": "https://gemnote-images-production.s3-us-west-2.amazonaws.com/images/images/000/001/275/full_size/kinto_ceramic_lab_tall_mug___brown.jpg?1510664123"
        },
        {
            "color": "White",
            "image_url": "https://gemnote-images-production.s3-us-west-2.amazonaws.com/images/images/000/001/274/full_size/kinto_ceramic_lab_tall_mug___white.jpg?1510664122"
        }
    ],
    "description": [
        "Handle designed to fit fingers comfortably",
        "Made of porcelain",
        "Mugs can be stacked together for compact storage",
        "Microwave and dishwasher safe"
    ],
    "weight": {
        "amount": 12.1,
        "unit": "ounce"
    },
    "price": {
        "amount": 23.1,
        "currency": "USD",
        "num_units": 1
    },
    "id": 1
}
```

Error response: code 404 and content:
```
{
    "message": "Product 10 doesn't exist. You have requested this URI [/products/10] but did you mean /products/<int:product_id> or /products ?"
}
```
