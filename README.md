## Project Description

With *dhl-express*, you can use DHL Express API to create and manage your shipping labels.

## Requirements

* Python (3.8 or higher)

## Installation

Install using pip

`pip install dhl-express`

## Usage

Use the `DHLService` class to create a new instance of the service.

```python
from dhl_express import DHLService

service = DHLService(
    api_key='YOUR_API_KEY',
    api_secret='YOUR_API_SECRET',
    test_mode=True
)
```

Validate shipment address using the `validate_address` method.

```python
service.validate_address(
    params={
        'type': 'delivery',
        'strictValidation': 'true',
        'postalCode': '12345',
        'cityName': 'New York',
        'countryCode': 'US',
    }
)
```

Create a shipment using the `create_shipment` method.

```python
service.create_shipment(
    **shipment_data
)
```

Get shipment status using the `get_shipment_status` method.

```python
service.get_shipment_status(
    shipment_id='1234567890'
)
```

Get shipment proof using the `get_shipment_proof` method.

```python
service.get_shipment_proof(
    shipment_id='1234567890'
)
```

## P.S.

If you find bugs, need help, or want to talk to the developers, please write an issue
on [GitHub](https://github.com/DCDie/dhl-express/issues).
