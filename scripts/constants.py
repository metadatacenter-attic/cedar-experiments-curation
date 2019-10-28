#!/usr/bin/python3

# Resources
RESOURCES_FOLDER = 'resources'

# Workspace
WORKSPACE_FOLDER = 'workspace'
SAMPLES_FOLDER = 'samples'
SOURCE_SAMPLES_FOLDER = 'source'
FILTERED_SAMPLES_FOLDER = 'filtered'

# Data download
NCBI_DOWNLOAD_URL = 'https://ftp.ncbi.nih.gov/biosample/biosample_set.xml.gz'
NCBI_SAMPLES_FOLDER_DEST = WORKSPACE_FOLDER  + '/' + SAMPLES_FOLDER + '/' + SOURCE_SAMPLES_FOLDER
NCBI_SAMPLES_FILE_DEST = 'biosample_set.xml.gz'

# Filtering
NCBI_FILTER_INPUT_FILE = NCBI_SAMPLES_FOLDER_DEST + '/' + NCBI_SAMPLES_FILE_DEST
NCBI_FILTER_OUTPUT_FOLDER = WORKSPACE_FOLDER  + '/' + SAMPLES_FOLDER + '/' + FILTERED_SAMPLES_FOLDER
NCBI_FILTER_OUTPUT_FILE = NCBI_FILTER_OUTPUT_FOLDER + '/' + 'biosample_filtered.xml'
NCBI_FILTER_RELEVANT_ATTS = ['sex', 'tissue', 'disease', 'cell_type', 'cell type', 'cell_line', 'cell line', 'ethnicity']
NCBI_FILTER_MIN_RELEVANT_ATTS = 3


SERVER = 'https://valuerecommender.metadatacenter.orgx'
TEMPLATE_ID = 'https://repo.metadatacenter.orgx/templates/cd03286e-96f4-47f9-a855-f46329b16920'