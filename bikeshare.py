import time
import pandas as pd
import numpy as np

#Lists
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january' , 'february' , 'march', 'april', 'may', 'june', 'all']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    city = input ("Enter  one of these cities (chicago, new york city, washington): ").lower()

    while city not in CITY_DATA:
        print("The city you entered: %s , is invalid " % (city))
        city = input ("Enter  one of these cities (chicago, new york city, washington): ")
    print("The city you selected is " + (city))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input ("Enter  one of the first six months or type all if you want all of them: ").lower()
    while month not in MONTHS:
        print(" The month you entered is invalid ")
    print("The month you selected is " + (month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ("Enter a week day: ")
    while day not in DAYS:
        print(" The day you entered is invalid ")
    print("The day you selected is " + (day))

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
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())

#check month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        df = df.loc[df['month'] == month,:]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: ".format(
        str(df['month'].mode().values[0]))
    )

    # display the most common day of week
    print("The most common day of the week: ".format(
        str(df['day_of_week'].mode().values[0]))
    )

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour: ".format(
        str(df['hour'].mode().values[0]))
    )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station is " + (start_station))


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("Most Common End Station is "+ (end_station))


    # TO DO: display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration= df['Trip Duration'].sum()
    print("Total Travel Time is %s in seconds " % (trip_duration))


    # TO DO: display mean travel time
    trip_mean = df['Trip Duration'].mean()
    print("Mean Travel Time is %s in seconds " % (trip_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("counts of various user types:")
    print(df['User Type'].value_counts())

    if city != 'washington':
        # Display counts of gender
        print("counts of gender:")
        print(df['Gender'].value_counts())


        # Display earliest, most recent, and most common year of birth
        print("The earliest birth year is: ".format(
            str(int(df['Birth Year'].min())))
        )
        print("The latest birth year is: ".format(
            str(int(df['Birth Year'].max())))
        )
        print("The most common birth year is: ".format(
            str(int(df['Birth Year'].mode().values[0])))
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """

    start_loc = 0
    end_loc = 5

    display_active = input("Do you want to see the raw data?: ").lower()

    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
