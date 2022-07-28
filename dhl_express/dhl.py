import base64
from typing import Dict

import requests


class DHLService:
    """
    Class to interact with DHL Express API
    """

    dhl_url = 'https://express.api.dhl.com/mydhlapi'
    dhl_test_url = 'https://express.api.dhl.com/mydhlapi/test'

    def __init__(self, api_key: str, api_secret: str, test_mode: bool = False):
        self.api_key = api_key
        self.api_secret = api_secret
        self.test_mode = test_mode
        self.endpoint = self.dhl_test_url if test_mode else self.dhl_url
        self.token = self.create_token()

        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Basic {self.token}'
        }

    def create_token(self):
        """
        Create a token for the API
        """
        token = '{username}:{password}'.format(username=self.api_key, password=self.api_secret)
        encoded_token = base64.b64encode(token.encode('utf-8'))
        encoded_token = str(encoded_token, 'utf-8')
        return encoded_token

    def validate_address(self, address: Dict) -> Dict:
        """
        Validate an address

        Example:
            {
                'type': 'delivery',
                'strictValidation': 'true',
                'postalCode': '12345',
                'cityName': 'New York',
                'countryCode': 'US',
            }
        """
        url = f'{self.endpoint}/address-validate'
        response = requests.get(url, headers=self.headers, params=address)
        response.raise_for_status()
        return response.json()

    def create_shipment(self, shipment_data: Dict) -> Dict:
        """
        Create a shipment

        Example:
            {
            "plannedShippingDateAndTime": "2019-08-04T14:00:31GMT+01:00",
            "pickup": {
                "isRequested": False,
                "closeTime": "18:00",
                "location": "reception",
                "specialInstructions": [
                    {
                        "value": "please ring door bell",
                        "typeCode": "TBD"
                    }
                ],
                "pickupDetails": {
                    "postalAddress": {
                        "postalCode": "14800",
                        "cityName": "Prague",
                        "countryCode": "CZ",
                        "provinceCode": "CZ",
                        "addressLine1": "V Parku 2308/10",
                        "addressLine2": "addres2",
                        "addressLine3": "addres3",
                        "countyName": "Central Bohemia",
                        "provinceName": "Central Bohemia",
                        "countryName": "Czech Republic"
                    },
                    "contactInformation": {
                        "email": "that@before.de",
                        "phone": "+1123456789",
                        "mobilePhone": "+60112345678",
                        "companyName": "Company Name",
                        "fullName": "John Brew"
                    },
                    "registrationNumbers": [
                        {
                            "typeCode": "VAT",
                            "number": "CZ123456789",
                            "issuerCountryCode": "CZ"
                        }
                    ],
                    "bankDetails": [
                        {
                            "name": "Russian Bank Name",
                            "settlementLocalCurrency": "RUB",
                            "settlementForeignCurrency": "USD"
                        }
                    ],
                    "typeCode": "business"
                },
                "pickupRequestorDetails": {
                    "postalAddress": {
                        "postalCode": "14800",
                        "cityName": "Prague",
                        "countryCode": "CZ",
                        "provinceCode": "CZ",
                        "addressLine1": "V Parku 2308/10",
                        "addressLine2": "addres2",
                        "addressLine3": "addres3",
                        "countyName": "Central Bohemia",
                        "provinceName": "Central Bohemia",
                        "countryName": "Czech Republic"
                    },
                    "contactInformation": {
                        "email": "that@before.de",
                        "phone": "+1123456789",
                        "mobilePhone": "+60112345678",
                        "companyName": "Company Name",
                        "fullName": "John Brew"
                    },
                    "registrationNumbers": [
                        {
                            "typeCode": "VAT",
                            "number": "CZ123456789",
                            "issuerCountryCode": "CZ"
                        }
                    ],
                    "bankDetails": [
                        {
                            "name": "Russian Bank Name",
                            "settlementLocalCurrency": "RUB",
                            "settlementForeignCurrency": "USD"
                        }
                    ],
                    "typeCode": "business"
                }
            },
            "productCode": "D",
            "localProductCode": "D",
            "getRateEstimates": True,
            "accounts": [
                {
                    "typeCode": "shipper",
                    "number": "123456789"
                }
            ],
            "customerReferences": [
                {
                    "value": "Customer reference",
                    "typeCode": "CU"
                }
            ],
            "customerDetails": {
                "shipperDetails": {
                    "postalAddress": {
                        "postalCode": "14800",
                        "cityName": "Prague",
                        "countryCode": "CZ",
                        "provinceCode": "CZ",
                        "addressLine1": "V Parku 2308/10",
                        "addressLine2": "addres2",
                        "addressLine3": "addres3",
                        "countyName": "Central Bohemia",
                        "provinceName": "Central Bohemia",
                        "countryName": "Czech Republic"
                    },
                    "contactInformation": {
                        "email": "that@before.de",
                        "phone": "+1123456789",
                        "mobilePhone": "+60112345678",
                        "companyName": "Company Name",
                        "fullName": "John Brew"
                    },
                    "registrationNumbers": [
                        {
                            "typeCode": "VAT",
                            "number": "CZ123456789",
                            "issuerCountryCode": "CZ"
                        }
                    ],
                    "bankDetails": [
                        {
                            "name": "Russian Bank Name",
                            "settlementLocalCurrency": "RUB",
                            "settlementForeignCurrency": "USD"
                        }
                    ],
                    "typeCode": "business"
                },
                "receiverDetails": {
                    "postalAddress": {
                        "postalCode": "14800",
                        "cityName": "Prague",
                        "countryCode": "CZ",
                        "provinceCode": "CZ",
                        "addressLine1": "V Parku 2308/10",
                        "addressLine2": "addres2",
                        "addressLine3": "addres3",
                        "countyName": "Central Bohemia",
                        "provinceName": "Central Bohemia",
                        "countryName": "Czech Republic"
                    },
                    "contactInformation": {
                        "email": "that@before.de",
                        "phone": "+1123456789",
                        "mobilePhone": "+60112345678",
                        "companyName": "Company Name",
                        "fullName": "John Brew"
                    },
                    "registrationNumbers": [
                        {
                            "typeCode": "VAT",
                            "number": "CZ123456789",
                            "issuerCountryCode": "CZ"
                        }
                    ],
                    "bankDetails": [
                        {
                            "name": "Russian Bank Name",
                            "settlementLocalCurrency": "RUB",
                            "settlementForeignCurrency": "USD"
                        }
                    ],
                    "typeCode": "business"
                },
                "buyerDetails": {
                    "postalAddress": {
                        "postalCode": "14800",
                        "cityName": "Prague",
                        "countryCode": "CZ",
                        "provinceCode": "CZ",
                        "addressLine1": "V Parku 2308/10",
                        "addressLine2": "addres2",
                        "addressLine3": "addres3",
                        "countyName": "Central Bohemia",
                        "provinceName": "Central Bohemia",
                        "countryName": "Czech Republic"
                    },
                    "contactInformation": {
                        "email": "buyer@domain.com",
                        "phone": "+44123456789",
                        "mobilePhone": "+42123456789",
                        "companyName": "Customer Company Name",
                        "fullName": "Mark Companer"
                    },
                    "registrationNumbers": [
                        {
                            "typeCode": "VAT",
                            "number": "CZ123456789",
                            "issuerCountryCode": "CZ"
                        }
                    ],
                    "bankDetails": [
                        {
                            "name": "Russian Bank Name",
                            "settlementLocalCurrency": "RUB",
                            "settlementForeignCurrency": "USD"
                        }
                    ],
                    "typeCode": "business"
                },
                "importerDetails": {
                    "postalAddress": {
                        "postalCode": "14800",
                        "cityName": "Prague",
                        "countryCode": "CZ",
                        "provinceCode": "CZ",
                        "addressLine1": "V Parku 2308/10",
                        "addressLine2": "addres2",
                        "addressLine3": "addres3",
                        "countyName": "Central Bohemia",
                        "provinceName": "Central Bohemia",
                        "countryName": "Czech Republic"
                    },
                    "contactInformation": {
                        "email": "that@before.de",
                        "phone": "+1123456789",
                        "mobilePhone": "+60112345678",
                        "companyName": "Company Name",
                        "fullName": "John Brew"
                    },
                    "registrationNumbers": [
                        {
                            "typeCode": "VAT",
                            "number": "CZ123456789",
                            "issuerCountryCode": "CZ"
                        }
                    ],
                    "bankDetails": [
                        {
                            "name": "Russian Bank Name",
                            "settlementLocalCurrency": "RUB",
                            "settlementForeignCurrency": "USD"
                        }
                    ],
                    "typeCode": "business"
                },
                "exporterDetails": {
                    "postalAddress": {
                        "postalCode": "14800",
                        "cityName": "Prague",
                        "countryCode": "CZ",
                        "provinceCode": "CZ",
                        "addressLine1": "V Parku 2308/10",
                        "addressLine2": "addres2",
                        "addressLine3": "addres3",
                        "countyName": "Central Bohemia",
                        "provinceName": "Central Bohemia",
                        "countryName": "Czech Republic"
                    },
                    "contactInformation": {
                        "email": "that@before.de",
                        "phone": "+1123456789",
                        "mobilePhone": "+60112345678",
                        "companyName": "Company Name",
                        "fullName": "John Brew"
                    },
                    "registrationNumbers": [
                        {
                            "typeCode": "VAT",
                            "number": "CZ123456789",
                            "issuerCountryCode": "CZ"
                        }
                    ],
                    "bankDetails": [
                        {
                            "name": "Russian Bank Name",
                            "settlementLocalCurrency": "RUB",
                            "settlementForeignCurrency": "USD"
                        }
                    ],
                    "typeCode": "business"
                },
                "sellerDetails": {
                    "postalAddress": {
                        "postalCode": "14800",
                        "cityName": "Prague",
                        "countryCode": "CZ",
                        "provinceCode": "CZ",
                        "addressLine1": "V Parku 2308/10",
                        "addressLine2": "addres2",
                        "addressLine3": "addres3",
                        "countyName": "Central Bohemia",
                        "provinceName": "Central Bohemia",
                        "countryName": "Czech Republic"
                    },
                    "contactInformation": {
                        "email": "that@before.de",
                        "phone": "+1123456789",
                        "mobilePhone": "+60112345678",
                        "companyName": "Company Name",
                        "fullName": "John Brew"
                    },
                    "registrationNumbers": [
                        {
                            "typeCode": "VAT",
                            "number": "CZ123456789",
                            "issuerCountryCode": "CZ"
                        }
                    ],
                    "bankDetails": [
                        {
                            "name": "Russian Bank Name",
                            "settlementLocalCurrency": "RUB",
                            "settlementForeignCurrency": "USD"
                        }
                    ],
                    "typeCode": "business"
                },
                "payerDetails": {
                    "postalAddress": {
                        "postalCode": "14800",
                        "cityName": "Prague",
                        "countryCode": "CZ",
                        "provinceCode": "CZ",
                        "addressLine1": "V Parku 2308/10",
                        "addressLine2": "addres2",
                        "addressLine3": "addres3",
                        "countyName": "Central Bohemia",
                        "provinceName": "Central Bohemia",
                        "countryName": "Czech Republic"
                    },
                    "contactInformation": {
                        "email": "that@before.de",
                        "phone": "+1123456789",
                        "mobilePhone": "+60112345678",
                        "companyName": "Company Name",
                        "fullName": "John Brew"
                    },
                    "registrationNumbers": [
                        {
                            "typeCode": "VAT",
                            "number": "CZ123456789",
                            "issuerCountryCode": "CZ"
                        }
                    ],
                    "bankDetails": [
                        {
                            "name": "Russian Bank Name",
                            "settlementLocalCurrency": "RUB",
                            "settlementForeignCurrency": "USD"
                        }
                    ],
                    "typeCode": "business"
                }
            },
            "content": {
                "packages": [
                    {
                        "typeCode": "2BP",
                        "weight": 22.501,
                        "dimensions": {
                            "length": 15.001,
                            "width": 15.001,
                            "height": 40.001
                        },
                        "customerReferences": [
                            {
                                "value": "Customer reference",
                                "typeCode": "CU"
                            }
                        ],
                        "description": "Piece content description",
                        "labelBarcodes": [
                            {
                                "position": "left",
                                "symbologyCode": "93",
                                "content": "string",
                                "textBelowBarcode": "text below left barcode"
                            }
                        ],
                        "labelText": [
                            {
                                "position": "left",
                                "caption": "text caption",
                                "value": "text value"
                            }
                        ],
                        "labelDescription": "bespoke label description"
                    }
                ],
                "isCustomsDeclarable": True,
                "declaredValue": 150,
                "declaredValueCurrency": "CZK",
                "exportDeclaration": {
                    "lineItems": [
                        {
                            "number": 1,
                            "description": "line item description",
                            "price": 150,
                            "quantity": {
                                "value": 1,
                                "unitOfMeasurement": "BOX"
                            },
                            "commodityCodes": [
                                {
                                    "typeCode": "outbound",
                                    "value": "HS1234567890"
                                }
                            ],
                            "exportReasonType": "permanent",
                            "manufacturerCountry": "CZ",
                            "exportControlClassificationNumber": "US123456789",
                            "weight": {
                                "netValue": 10,
                                "grossValue": 10
                            },
                            "isTaxesPaid": True,
                            "additionalInformation": [
                                "string"
                            ],
                            "customerReferences": [
                                {
                                    "typeCode": "AFE",
                                    "value": "custref123"
                                }
                            ],
                            "customsDocuments": [
                                {
                                    "typeCode": "972",
                                    "value": "custdoc456"
                                }
                            ]
                        }
                    ],
                    "invoice": {
                        "number": "12345-ABC",
                        "date": "2020-03-18",
                        "signatureName": "Brewer",
                        "signatureTitle": "Mr.",
                        "signatureImage": "Base64 encoded image",
                        "instructions": [
                            "string"
                        ],
                        "customerDataTextEntries": [
                            "string"
                        ],
                        "totalNetWeight": 999999999999,
                        "totalGrossWeight": 999999999999,
                        "customerReferences": [
                            {
                                "typeCode": "CU",
                                "value": "custref112"
                            }
                        ],
                        "termsOfPayment": "100 days"
                    },
                    "remarks": [
                        {
                            "value": "declaration remark"
                        }
                    ],
                    "additionalCharges": [
                        {
                            "value": 10,
                            "caption": "fee",
                            "typeCode": "freight"
                        }
                    ],
                    "destinationPortName": "port details",
                    "placeOfIncoterm": "port of departure or destination details",
                    "payerVATNumber": "12345ED",
                    "recipientReference": "recipient reference",
                    "exporter": {
                        "id": "123",
                        "code": "EXPCZ"
                    },
                    "packageMarks": "marks",
                    "declarationNotes": [
                        {
                            "value": "up to three declaration notes"
                        }
                    ],
                    "exportReference": "export reference",
                    "exportReason": "export reason",
                    "exportReasonType": "permanent",
                    "licenses": [
                        {
                            "typeCode": "export",
                            "value": "license"
                        }
                    ],
                    "shipmentType": "personal",
                    "customsDocuments": [
                        {
                            "typeCode": "972",
                            "value": "custdoc445"
                        }
                    ]
                },
                "description": "shipment description",
                "USFilingTypeValue": "12345",
                "incoterm": "DAP",
                "unitOfMeasurement": "metric"
            },
            "documentImages": [
                {
                    "typeCode": "INV",
                    "imageFormat": "PDF",
                    "content": "base64 encoded image"
                }
            ],
            "onDemandDelivery": {
                "deliveryOption": "servicepoint",
                "location": "front door",
                "specialInstructions": "ringe twice",
                "gateCode": "1234",
                "whereToLeave": "concierge",
                "neighbourName": "Mr.Dan",
                "neighbourHouseNumber": "777",
                "authorizerName": "Newman",
                "servicePointId": "SPL123",
                "requestedDeliveryDate": "2020-04-20"
            },
            "requestOndemandDeliveryURL": True,
            "shipmentNotification": [
                {
                    "typeCode": "email",
                    "receiverId": "receiver@email.com",
                    "languageCode": "eng",
                    "languageCountryCode": "UK",
                    "bespokeMessage": "message to be included in the notification"
                }
            ],
            "prepaidCharges": [
                {
                    "typeCode": "freight",
                    "currency": "CZK",
                    "value": 200,
                    "method": "cash"
                }
            ],
            "getTransliteratedResponse": True,
            "estimatedDeliveryDate": {
                "isRequested": False,
                "typeCode": "QDDC"
            },
            "getAdditionalInformation": [
                {
                    "typeCode": "pickupDetails",
                    "isRequested": True
                }
            ],
            "parentShipment": {
                "productCode": "s",
                "packagesCount": 1
            }
        }
        """
        url = f'{self.endpoint}/shipments'
        response = requests.post(url, headers=self.headers, json=shipment_data)
        response.raise_for_status()
        return response.json()

    def get_shipment_status(self, shipment_id: str) -> Dict:
        """
        Check the status of a shipment
        """
        url = f'{self.endpoint}/shipments/{shipment_id}/tracking'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_shipment_proof(self, shipment_id: str) -> Dict:
        """
        Get the proofs of a shipment
        """
        url = f'{self.endpoint}/shipments/{shipment_id}/proof-of-delivery'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
