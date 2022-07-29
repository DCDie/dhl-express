from typing import Dict
from urllib.parse import urljoin

from requests import Session, Response
from requests.auth import AuthBase, HTTPBasicAuth


__all__ = (
    'DHLService',
    'DHLServiceSession'
)


class DHLServiceSession(Session):
    def __init__(self, base_url: str, auth: AuthBase):
        super(DHLServiceSession, self).__init__()

        self.base_url = base_url
        self.auth = auth

    def request(self, method: str, url: str, **kwargs) -> Response:
        kwargs.setdefault('headers', dict())
        kwargs['headers'].setdefault('Accept', 'Application/JSON')
        kwargs['headers'].setdefault('Content-Type', 'Application/JSON')
        return super(DHLServiceSession, self).request(method, urljoin(self.base_url, url), **kwargs)

    @classmethod
    def from_credentials(cls, api_key: str, api_secret: str, base_url: str = None):
        return cls(base_url=base_url, auth=HTTPBasicAuth(username=api_key, password=api_secret))

    def shipment_create(self, json: Dict, **kwargs) -> Response:
        return self.post('shipments', json=json, **kwargs)

    def shipment_tracking(self, shipment_id: str, **kwargs) -> Response:
        return self.get(f'shipments/{shipment_id}/tracking', **kwargs)

    def shipment_proof_of_delivery(self, shipment_id: str, **kwargs) -> Response:
        return self.get(f'shipments/{shipment_id}/proof-of-delivery', **kwargs)

    def address_validate(self, params: Dict, **kwargs) -> Response:
        return self.get('address-validate', params=params, **kwargs)


class DHLService:
    """
    Class to interact with DHL Express API
    """

    dhl_base_url = 'https://express.api.dhl.com/mydhlapi/'
    dhl_test_url = 'https://express.api.dhl.com/mydhlapi/test/'

    def __init__(self, api_key: str, api_secret: str, test_mode: bool = False):
        self.session = DHLServiceSession.from_credentials(
            api_key=api_key,
            api_secret=api_secret,
            base_url=self.dhl_test_url if test_mode else self.dhl_base_url
        )

    def validate_address(self, params: Dict) -> Dict:
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
        response = self.session.address_validate(params=params)
        response.raise_for_status()
        return response.json()

    def create_shipment(self, json: Dict) -> Dict:
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
        response = self.session.shipment_create(json=json)
        response.raise_for_status()
        return response.json()

    def get_shipment_status(self, shipment_id: str) -> Dict:
        """
        Check the status of a shipment
        """
        response = self.session.shipment_tracking(shipment_id=shipment_id)
        response.raise_for_status()
        return response.json()

    def get_shipment_proof(self, shipment_id: str) -> Dict:
        """
        Get the proofs of a shipment
        """
        response = self.session.shipment_proof_of_delivery(shipment_id=shipment_id)
        response.raise_for_status()
        return response.json()
