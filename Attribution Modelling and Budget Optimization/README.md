# Attribution Modelling

-   Attribution Modeling is a set of rules for assigning credit to the various touch points in the conversion path.
-   This method helps us understand how the prospect customer travels through the path to purchase.
-   There are many attribution models available, a specific model should be chosen based on the products sold and the length of buying cycle.
-   We use the Criteo Attribution modeling dataset to build attribution models which optimize the budget allocation for various marketing campaigns

## Attribution Modelling Techniques

### Single Touch Attribution

1. First Touch Attribution

2. Last Touch Attribution

### Multi Touch Attribution

1. Linear Attribution

2. Time-Decay Attribution

3. U-Shape Attribution

### Data-Driven Attribution

1. Logistic Regression

2. LSTM (Long Short Term Memory)

3. LSTM with Attention

![](https://lh3.googleusercontent.com/TZrt_y_PSTGfJfm66TxihIMw9Cr7iB4-qOlBMpILRBBoIHGbSaf10JQkICmN_Uc6ADAhEGS_fiGMhgpFJgcwVlct3QEvTinBfRBsh8SM7zuAK_oc4W_bQ3fyGymBZFhloUoCONUI)

## Dataset Description

This dataset represents a sample of 30 days of Criteo live traffic data. Each line corresponds to one impression (a banner) that was displayed to a user. For each banner we have detailed information about the context, if it was clicked, if it led to a conversion and if it led to a conversion that was attributed to Criteo or not.

-   timestamp: timestamp of the impression (starting from 0 for the first impression). The dataset is sorted according to timestamp.
-   uid: a unique user identifier
-   campaign: a unique identifier for the campaign
-   conversion: 1 if there was a conversion in the 30 days after the impression (independently of whether this impression was last click or not)
-   conversion_timestamp: the timestamp of the conversion or -1 if no conversion was observed
-   conversion_id: a unique identifier for each conversion (so that timelines can be reconstructed if needed). -1 if there was no conversion
-   attribution: 1 if the conversion was attributed to Criteo, 0 otherwise
-   click: 1 if the impression was clicked, 0 otherwise
-   click_pos: the position of the click before a conversion (0 for first-click)
-   click_nb: number of clicks. More than 1 if there was several clicks before a conversion
-   cost: the price paid by Criteo for this display (disclaimer: not the real price, only a transformed version of it)
-   cpo: the cost-per-order in case of attributed conversion (disclaimer: not the real price, only a transformed version of it)
-   time_since_last_click: the time since the last click (in s) for the given impression
-   cat(1-9): contextual features associated to the display. Can be used to learn the click/conversion models. We do not disclose the meaning of these features but it is not relevant for this study. Each column is a categorical variable. In the experiments, they are mapped to a fixed dimensionality space using the Hashing Trick (see paper for reference).
