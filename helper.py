# import the necessary libraries
import pandas as pd
import numpy as np
import math
import json
from datetime import datetime, date
import matplotlib.pyplot as plt
import seaborn as sns



# Create a dataframe per customer
def cust_tran_summary(transcript2, profile_clean):
    '''
    This function summarizes the customer purchases for analysis
    
    INPUT:
    transcript - dataframe containing cleaned records for transactions, offers received, offers viewed, 
    and offers completed
    
    profile_clean - dataframe containing cleaned demographic data for each customer
    
    OUTPUT:
    profile_trans - profile dataframe including customer purchase summary
    '''    
    
    # Group the purchases by customer id 
    trans_events = transcript2.groupby('customer_id')
    # Calculate the total purchsed amount by customer
    purchase_total = trans_events[['customer_id', 'amount']].sum()
    purchase_total.rename(columns={'amount':'purchase_total'}, inplace=True)    
    
    # Calculate the average purchsed amount by customer
    purchase_ave = trans_events[['customer_id', 'amount']].mean()
    purchase_ave.rename(columns={'amount':'purchase_ave'}, inplace=True)      
    
    # Calculate the number of purchses by customer
    transactions = trans_events[['customer_id', 'amount']].count()
    transactions.rename(columns={'amount':'num_trxns'}, inplace=True)    
    transactions.drop('customer_id', axis = 1, inplace = True)
    
    # Calculate the total reward received by customer    
    total_reward = trans_events[['customer_id', 'reward_received']].sum()
    total_reward.rename(columns={'reward_received':'total_reward'}, inplace=True)     
    
    # Calculate the number of offers received by customer    
    off_received = trans_events[['customer_id', 'event_offer_received']].sum()
    off_received.rename(columns={'event_offer_received':'off_received'}, inplace=True)  
    
    # Calculate the number of offers viewed by customer    
    off_viewed = trans_events[['customer_id', 'event_offer_viewed']].sum()
    off_viewed.rename(columns={'event_offer_viewed':'off_viewed'}, inplace=True)    
    
    # Calculate the number of offers completed by customer    
    off_completed = trans_events[['customer_id', 'event_offer_completed']].sum()
    off_completed.rename(columns={'event_offer_completed':'off_completed'}, inplace=True)    
 
    # Calculate the number of bogo offers types by customer
    bogo = transcript2[transcript2.offer_type == 'bogo'].groupby('customer_id')
    bogo_received = bogo[['customer_id', 'event_offer_received']].sum()
    bogo_received.rename(columns={'event_offer_received':'bogo_received'}, inplace=True)
    bogo_viewed = bogo[['customer_id', 'event_offer_viewed']].sum()
    bogo_viewed.rename(columns={'event_offer_viewed':'bogo_viewed'}, inplace=True)
    bogo_completed = bogo[['customer_id', 'event_offer_completed']].sum()
    bogo_completed.rename(columns={'event_offer_completed':'bogo_completed'}, inplace=True)    
    
    # Calculate the number of discount offers types by customer
    discount = transcript2[transcript2.offer_type == 'discount'].groupby('customer_id')
    discount_received = discount[['customer_id', 'event_offer_received']].sum()
    discount_received.rename(columns={'event_offer_received':'discount_received'}, inplace=True)
    discount_viewed = discount[['customer_id', 'event_offer_viewed']].sum()
    discount_viewed.rename(columns={'event_offer_viewed':'discount_viewed'}, inplace=True)
    discount_completed = discount[['customer_id', 'event_offer_completed']].sum()
    discount_completed.rename(columns={'event_offer_completed':'discount_completed'}, inplace=True)      
    
    # Calculate the number of informational offers types by customer
    info = transcript2[transcript2.offer_type == 'informational'].groupby('customer_id')
    info_received = info[['customer_id', 'event_offer_received']].sum()
    info_received.rename(columns={'event_offer_received':'info_received'}, inplace=True)    
    info_viewed = info[['customer_id', 'event_offer_viewed']].sum()
    info_viewed.rename(columns={'event_offer_viewed':'info_viewed'}, inplace=True)
    
    #Merge transaction summary data to the profile data
    profile_trans = pd.merge(profile_clean, purchase_total, on = 'customer_id', how = 'left')
    profile_trans = pd.merge(profile_trans, purchase_ave, on = 'customer_id', how = 'left')  
    profile_trans = pd.merge(profile_trans, transactions, on = 'customer_id', how = 'left') 
    profile_trans = pd.merge(profile_trans, off_received, on = 'customer_id', how = 'left') 
    profile_trans = pd.merge(profile_trans, off_viewed, on = 'customer_id', how = 'left')      
    profile_trans = pd.merge(profile_trans, off_completed, on = 'customer_id', how = 'left')  
    profile_trans = pd.merge(profile_trans, bogo_received, on = 'customer_id', how = 'left') 
    profile_trans = pd.merge(profile_trans, bogo_viewed, on = 'customer_id', how = 'left')    
    profile_trans = pd.merge(profile_trans, bogo_completed, on = 'customer_id', how = 'left')    
    profile_trans = pd.merge(profile_trans, discount_received, on = 'customer_id', how = 'left') 
    profile_trans = pd.merge(profile_trans, discount_viewed, on = 'customer_id', how = 'left')    
    profile_trans = pd.merge(profile_trans, discount_completed, on = 'customer_id', how = 'left')    
    profile_trans = pd.merge(profile_trans, info_received, on = 'customer_id', how = 'left')   
    profile_trans = pd.merge(profile_trans, info_viewed, on = 'customer_id', how = 'left')      
    profile_trans = pd.merge(profile_trans, total_reward, on = 'customer_id', how = 'left')  
    profile_trans['purchase_total'].fillna(0, inplace=True)
    profile_trans['purchase_ave'].fillna(0, inplace=True)    
    profile_trans['num_trxns'].fillna(0, inplace=True)
    profile_trans['off_received'].fillna(0, inplace=True)
    profile_trans['off_viewed'].fillna(0, inplace=True)
    profile_trans['off_completed'].fillna(0, inplace=True)    
    profile_trans['bogo_received'].fillna(0, inplace=True)  
    profile_trans['bogo_viewed'].fillna(0, inplace=True)   
    profile_trans['bogo_completed'].fillna(0, inplace=True)    
    profile_trans['discount_received'].fillna(0, inplace=True)
    profile_trans['discount_viewed'].fillna(0, inplace=True)    
    profile_trans['discount_completed'].fillna(0, inplace=True)    
    profile_trans['info_received'].fillna(0, inplace=True)    
    profile_trans['info_viewed'].fillna(0, inplace=True)      
    profile_trans['total_reward'].fillna(0, inplace=True)
    profile_trans['total_net_value'] = profile_trans['purchase_total'] - profile_trans['total_reward']
    return profile_trans



# Create function to create one line per customer/offer
def cust_offer(starbucks_data, profile_clean, portfolio_clean):
    '''
    This function cleans the starbucks_data and creates a new dataframe with one line per customer/offer/transaction
    for analysis    
    
    INPUT:
    starbucks_data - cleaned merged dataframe
   
    starbucks_data - cleaned merged dataframe
    profile_clean - cleaned profile dataframe
    portfolio_clean - cleaned portfolio dataframe
    
    OUTPUT:
    cust_offer_details - dataframe with one line per customer/offer
    '''
    
    # Create new time completed column getting the max value for each customer/time combination
    starbucks = starbucks_data
    trans_temp = starbucks.groupby(['customer_id', 'time'])['time_completed'].max().reset_index()
    trans_temp.rename(columns={'time_completed':'time_completed_max'}, inplace=True)
    
    # Merge new time_completed column back into the dataframe
    trans_temp2 = pd.merge(starbucks, trans_temp, on = ['customer_id', 'time'], how = 'left')
    
    # Create new offer id column getting the first value for each customer/time combination
    # First sort the data to get the correct 'first' value in the sort
    transcript_clean2 = starbucks.sort_values(by=['customer_id', 'time', 'event'])
    # Create the new column
    trans_temp3 = transcript_clean2.groupby(['customer_id', 'time'])['offer_id'].first().reset_index()
    trans_temp3.rename(columns={'offer_id':'offer_id_tmp'}, inplace=True)
    
    # Merge new offer_id column back into the dataframe
    trans_temp4 = pd.merge(trans_temp2, trans_temp3, on = ['customer_id', 'time'], how = 'left')
    # Correct the offer id for cases where one offer was overlapped with another
    trans_temp4['offer_id_new'] = np.where(trans_temp4['offer_id'].isna(), trans_temp4['offer_id_tmp'], trans_temp4['offer_id'])
    
    # Drop the original columns being replaced
    trans_temp4.drop(['event', 'time', 'offer_id', 'time_completed', 'offer_id_tmp'], axis = 1, inplace = True)
    
    # Rename the new columns
    trans_temp4.rename(columns={'offer_id_new':'offer_id', 'time_completed_max':'time_completed'}, inplace=True)
       
    # Create a dataframe of the purchases not associated with an offer
    no_offer = trans_temp4[trans_temp4.offer_id.isnull()]
    #no_offer = no_offer.reindex(sorted(no_offer.columns), axis=1)
    
    # Get one row of data per customer/offer id
    offer = trans_temp4[trans_temp4.offer_id.notnull()]
    offer2 = offer.groupby(['customer_id', 'offer_id'], as_index=False).max()
    #offer2 = offer2.reindex(sorted(offer2.columns), axis=1)
    
    #Merge category values back in since max function does not work on them
    offer3 = pd.merge(offer2, profile_clean[['customer_id', 'age_cat', 'income_cat', 'member_cat']], on = ['customer_id'], how = 'left')
    offer4 = pd.merge(offer3, portfolio_clean[['offer_id', 'offer_type']], on = ['offer_id'], how = 'left')
    
    # Combine the no offers and offers together
    cust_offer = pd.concat([offer4, no_offer], sort = True)
    cust_offer = cust_offer.sort_values(by=['customer_id'])
   
    # Rename the missing offer type to No offer 
    cust_offer['offer_type'] = cust_offer['offer_type'].replace({None: 'No offer'})
    
    #Create a new column called viewed_prior to code those who viewed the offer after their purchase as 'not 'viewed'
    cust_offer['viewed_prior'] = np.where(cust_offer['time_viewed'] > cust_offer['time_completed'],
                                                  0, cust_offer['event_offer_viewed'])
    
    # Create a new column called offer_id_clean where those who have not viewed the offer or viewed the offer after their purchase
    # are considered to have been given no offer
    cust_offer['offer_id_clean'] = np.where(cust_offer['viewed_prior'] == 1, cust_offer['offer_id'], None)

    # Create a new column called offer_type2 where those who have not viewed the offer or viewed the offer after their 
    # purchase are considered to have been given no offer
    #cust_offer['offer_type2'] = np.where(cust_offer['viewed_prior'] == 1, cust_offer['offer_type'], None)
    
    # Create a new column called responded_to_offer for those who viewed (prior to purchase) and completed the offer 
    cust_offer['responded_to_offer'] = np.where((cust_offer['viewed_prior'] == 1) & 
                                                 (cust_offer['event_offer_completed'] == 1), 1, 0)
    
    #Create a new column called offer_responded_to to categorize the offer types customers responded to
    #cust_offer['offer_responded_to'] = np.select([(cust_offer['offer_type'] == 'bogo') & (cust_offer['responded_to_offer'] == 1),
                                                   #(cust_offer['offer_type'] == 'discount') & (cust_offer['responded_to_offer'] == 1)],
                                                   #['bogo', 'discount'], 'no offer response')
     
    #Create a new column called offer_id_responded_to to categorize the offer id customers responded to
    #cust_offer['offer_id_responded_to'] = np.where((cust_offer['offer_responded_to'] == 'no offer response'), 'no offer response', 
                                                   #cust_offer['offer_id_clean']) 
                                                     
    #fill in nan with 0 for reward
    cust_offer['reward_received'].fillna(0, inplace=True)
    
    #Calculate the net total revenue (purchases minus the rewards)
    cust_offer['net_value'] = cust_offer['amount'] - cust_offer['reward_received']
    
    cust_offer_details = cust_offer
      
    return cust_offer_details


# Create dataframe for model building
def modeling_data(cust_offer_details):
    '''
    This function cleans the cust_offer_details data for model building
    
    INPUT:
    cust_offer_details - cleaned starbucks dataframe
    
    OUTPUT:
    model_data - dataframe for use with model building
    '''
    
    # Keep only the necessary columns
    m_data = cust_offer_details[['customer_id', 'gender', 'event_offer_received', 'event_offer_viewed', 'event_offer_completed', 
                                 'event_transaction', 'amount', 'offer_id', 'offer_type', 'duration', 'difficulty', 'reward_received', 
                                 'ch__email', 'ch__mobile', 'ch__social', 'ch__web', 'responded_to_offer', 'age', 'income', 'days_member', 
                                 'member_year', 'member_month', 'net_value']]
    
    # Replace missing values with 0
    data_subset = m_data.fillna(0)
      
    #Replace text values with numeric values
    data_subset.replace({'gender' : { 'F' : 0, 'M' : 1, 'O' : 2 }}, inplace=True)
    data_subset.replace({'offer_id' : {'0': 0, 'bogo1' : 1, 'bogo2' : 2, 'bogo3' : 3, 'bogo4' : 4, 'discount1' : 5, 'discount2' : 6,
                                       'discount3' : 7, 'discount4' : 8, 'info1' : 9, 'info2' : 10}}, inplace=True)
    data_subset.replace({'offer_type' : {'No offer' : 0, 'bogo' : 1, 'discount' : 2, 'informational' : 3 }}, inplace=True)
      
    #Create age, income and member days bins (with more categories than in EDA)
    data_subset['age_cat'] = pd.cut(m_data.age, bins=[0,10,20,30,40,50,60,70,80,90,100,110], labels=[1,2,3,4,5,6,7,8,9,10,11])
    
    #Create categorical column for income
    data_subset['income_cat'] = pd.cut(m_data.income, bins=[0,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,
                                                             120000,130000], labels=[1,2,3,4,5,6,7,8,9,10,11,12,13])
    
    #Create categorical column for days as a member
    data_subset['member_cat'] = pd.cut(m_data.days_member, bins=[0,500,1500,2000,2500,3000], labels=[1,2,3,4,5])
    
    model_data = data_subset
    
    return model_data                           
                                 
                                 
                                 
                                 
         