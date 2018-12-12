# Import library
import pandas as pd
import os
import sys
import glob

# Get feature vector directory
fv_dir = sys.argv[1]
data_path = os.path.join(fv_dir, '*.csv')
files = glob.glob(data_path)

# Combine csv files
combined_csv = pd.concat([pd.read_csv(file) for file in files])

# Make directory for saving export csv file
export_dir = "C:/Users/rohuj/Desktop/ras_cam"

try:
        if not os.path.isdir(export_dir) :
                os.mkdir(export_dir)
except OSError as e:
        if e.errno != errno.EEXIST:
                print("Failed to create directory\n")
                raise

# Export csv file
combined_csv.to_csv(os.path.join(export_dir, "aligned_extra_hw_features.csv"), index = False)

