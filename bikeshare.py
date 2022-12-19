import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_inputs=['new york city', 'chicago', 'washington']
Month_input=['January', 'February', 'March', 'April', 'May', 'June', 'all']
Month_without_all=['January', 'February', 'March', 'April', 'May', 'June']
days_input=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Enter your code here
    while True:
        city = input("please enter the city name: ")
        city = city.lower()
        if city not in ['chicago' , 'new york city' , 'washington']:
            print (" please enter city between chicago , new york city , washington")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("Please choose the month (January, February, March, April, May, June ) or 'all' if you all data").title()
      if month not in Month_input:
        print("Please choose correct Month.")
        continue
      elif month not in Month_without_all:
          print("Please choose correct Month.")
      else:
        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("Please choose the day ( Saturday,Sunday, Monday, Tuesday, Wednesday, Thursday, Friday)  or 'all' if you all data.").title()
      if day not in days_input:
        print("Please choose correct Day.")
        continue
      else:
        break
        
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        month = Month_without_all.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]
    else:
        month = Month.index(month) + 1

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('most commonly start station: {}'.format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('most commonly end station: {}' .format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station']).count()
    print('most commonly frequent combination of start station and end station trip:[', start_station, " && ", end_station,']')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:{}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time: {}' .format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('user Types: {}'.format(user_types))

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('count gender : {}'.format(gender))
    except:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('earliest year: {}'.format(earliest_year))

        most_recent_year = df['Birth Year'].max()
        print('most recent year: {}'.format(most_recent_year))

        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('most common year: {}'.format(most_common_year))
    except KeyError:
        print('stats cannot be calculated because it is  not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    while True:
        x=5
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        if view_data.lower() == 'yes':
            print(df.head(x))
            if input ("Do you wish to continue?: ").lower() =='no':
                break
            else:
             print(df.head(x+5))
        else:
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
