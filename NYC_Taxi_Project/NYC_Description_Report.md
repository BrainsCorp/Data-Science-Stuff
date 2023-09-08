
# NYC Taxi Project

The Project aims to take the NYC taxi January 2023 dataset for exploratory analysis. So, as to highlight main patterns and gather useful insights.

### Dataset source :point_right: [link to source website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

### Data Dictionary :star2: [link to data dictionary](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)

*some main attributes to look at -*
* Vendor_id
* tep_pickup_datetime
* tep_dropoff_datetime
* pickup_locationID
* dropoff_locationID
* payment_type
* ratecodeID
* total_amount
* fare_amount

### Questionare
Questions are the first thing before getting hands dirty on the dataset. We should be able to ask right questions so, to able to head towards correct way.

**Some Questions explored in notebook are:**
* Most popular mode of payment by volumn?
* Most busy days of a week?
* Comparsion of pickup and dropoff timings during the day.
* Most popular pickup and dropoff location?
* Revenue by ratecodes
* **. . .**


## Key Findings
1. **Missing Values**
    * > the dataset contains total of 70000+ records whose any column contains missing values.
    * > It strange to note that all such records have passenger count and ratecode missing thought trip has some fare amount associated with it.
    * > Could be because of a null trips or drivers just roam around the city.

2. **Most Busy weekday**
    * > Although, all weekdays including weekends cross 4 lakh number, Tuesday have the highest number of trips at nearly 5 lakhs.

3. **Most Prefered type of Payment**
    * > Cash is most suitable payment type with almost 79 percent payment done in this mode only (24 lakh+).
    * > Credit card account for only 2% of total figure with precisely 71743 payments only. Additionaly, it is bit of strange to note that all records which have passenger count and ratecodeID equal to Nan have done payment by credit card only.

4. **Peak time during the Day**
    * > Afternoon to Evening mainly between (12PM to 7PM) have recorded most number of trips with reaching its peak at 6PM
    * > Also, trips in morning (6AM to 10AM) increases at rapid rate mainly because of people getting to work.
    * > Late Night (1AM to 5AM) seen lowest trips, with lowest recored at 5AM.

5. **Comparision PickUp and dropoff hour**
    * > Late Night have more dropoffs and Morings have more PickUps, which bit obivious but verified using data analysis.

**More to Come...**