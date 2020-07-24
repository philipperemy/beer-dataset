# Largest Beer Database :beers:

Scraped from https://brewerydb.com/ in late 2019.

Perfect for some data science / ML analysis.

To re-download the whole database, you will need a pro account. Support them if you are into beers!

It contains **30,280** records in JSON format. I also provide a script `download.py` to download the images of the labels.

An example of a beer data point:
```json
{
      "id": "1Ggl3w",
      "name": "Acres O' Green Irish Red",
      "nameDisplay": "Acres O' Green Irish Red",
      "description": "Leprechauns and humans alike love to dance a jig while celebrating with our Irish Red. The complexity of malts converges into a smooth mouthfeel, lightly punctuated with a dash of subtle hoppiness.",
      "abv": "6",
      "ibu": "32",
      "glasswareId": 5,
      "srmId": 41,
      "availableId": 1,
      "styleId": 22,
      "isOrganic": "N",
      "isRetired": "N",
      "labels": {
        "icon": "https://brewerydb-images.s3.amazonaws.com/beer/1Ggl3w/upload_QP9FmU-icon.png",
        "medium": "https://brewerydb-images.s3.amazonaws.com/beer/1Ggl3w/upload_QP9FmU-medium.png",
        "large": "https://brewerydb-images.s3.amazonaws.com/beer/1Ggl3w/upload_QP9FmU-large.png",
        "contentAwareIcon": "https://brewerydb-images.s3.amazonaws.com/beer/1Ggl3w/upload_QP9FmU-contentAwareIcon.png",
        "contentAwareMedium": "https://brewerydb-images.s3.amazonaws.com/beer/1Ggl3w/upload_QP9FmU-contentAwareMedium.png",
        "contentAwareLarge": "https://brewerydb-images.s3.amazonaws.com/beer/1Ggl3w/upload_QP9FmU-contentAwareLarge.png"
      },
      "status": "verified",
      "statusDisplay": "Verified",
      "servingTemperature": "cool",
      "servingTemperatureDisplay": "Cool - (8-12C/45-54F)",
      "createDate": "2013-08-13 18:54:26",
      "updateDate": "2015-12-17 04:41:48",
      "glass": {
        "id": 5,
        "name": "Pint",
        "createDate": "2012-01-03 02:41:33"
      },
      "srm": {
        "id": 41,
        "name": "Over 40",
        "hex": "000000"
      },
      "available": {
        "id": 1,
        "name": "Year Round",
        "description": "Available year round as a staple beer."
      },
      "style": {
        "id": 22,
        "categoryId": 2,
        "category": {
          "id": 2,
          "name": "Irish Origin Ales",
          "createDate": "2012-03-21 20:06:45"
        },
        "name": "Irish-Style Red Ale",
        "shortName": "Irish Red",
        "description": "Irish-style red ales range from light red-amber-copper to light brown in color. These ales have a medium hop bitterness and flavor. They often don't have hop aroma. Irish-style red ales have low to medium candy-like caramel malt sweetness and may have a balanced subtle degree of roast barley or roast malt character and complexity.  Irish-style Red Ales have a medium body. The style may have low levels of fruity-ester flavor and aroma. Diacetyl should be absent or at very low levels. Chill haze is allowable at cold temperatures. Slight yeast haze is acceptable for bottle-conditioned products.",
        "ibuMin": "20",
        "ibuMax": "28",
        "abvMin": "4",
        "abvMax": "4.5",
        "srmMin": "11",
        "srmMax": "18",
        "ogMin": "1.04",
        "fgMin": "1.01",
        "fgMax": "1.014",
        "createDate": "2012-03-21 20:06:45",
        "updateDate": "2015-04-07 15:23:38"
      }
}
```
