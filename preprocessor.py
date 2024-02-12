def preprocess_captions(captions, images_features):
    """
    Preprocesses captions and converts them into a dictionary format.

    Args:
    - captions (list): List of captions, where each caption is a string containing the image name and caption separated by a tab.
    - images_features (list): List of image names with features predicted by ResNet50.

    Returns:
    - captions_dict (dict): Dictionary where keys are image names and values are lists of preprocessed captions.
    """

    # Initialize an empty dictionary to store preprocessed captions
    captions_dict = {}

    # Iterate through each caption
    for caption in captions:
        try:
            # Split the caption at '\t' to extract image name and caption text
            img_name = caption.split('\t')[0][:-2] 
            caption_text = caption.split('\t')[1]
            
            # Check if the image name is in the list of images with features
            if img_name in images_features:
                # Add the caption to the dictionary under the corresponding image name
                if img_name not in captions_dict:
                    captions_dict[img_name] = [caption_text]
                else:
                    captions_dict[img_name].append(caption_text)
        except:
            pass # Handle exceptions gracefully, if any
    
    # Define a function to preprocess individual captions
    def process(txt):
        return "startofseq " + txt.lower() + " endofseq"
    
    # Preprocess each caption in the dictionary
    for image, captions in captions_dict.items():
        for idx, caption in enumerate(captions):
            captions_dict[image][idx] = process(caption)
    
    # Create a vocabulary for words in captions
    word_counts = {}
    word_index = 1
    for image, captions in captions_dict.items():
        for caption in captions:
            for word in caption.split():
                if word not in word_counts:
                    word_counts[word] = word_index
                    word_index += 1
    
    # Convert words in captions to integers based on the vocabulary
    for image, captions in captions_dict.items():
        for caption in captions:
            encoded_caption = [word_counts[word] for word in caption.split()]
            captions_dict[image][captions.index(caption)] = encoded_caption
    
    return word_counts,captions_dict
