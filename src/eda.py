# Load NBA data from CSV
def load_data(filepath):
    """Load NBA data from CSV."""
    df = pd.read_csv(filepath)
    return df

def convert_time_float(df, column):
    """Convert single MM:SS string to decimal minutes."""
   if isinstance(time_string, float):
        return time_string
    minutes, seconds = time_string.split(':')
    return float(minutes) + float(seconds) / 60

def summary_statistics(df, columns):
    """Return summary stats for specified columns."""
    metrics = ['count', 'mean', 'median', 'std', 'min', 'max']
    return df[columns].agg(metrics)

def plot_distributions(df, columns):
    """Plot histograms for specified columns."""
    # code here
    pass

def detect_outliers(df, column, method='iqr'):
    """Detect outliers using IQR method."""
    # code here
    pass