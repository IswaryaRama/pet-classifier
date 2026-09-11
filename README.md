# Pet Classifier (Cats vs Dogs)

A binary image classifier built with TensorFlow/Keras that predicts whether an image contains a **cat** or a **dog**, using a small Convolutional Neural Network (CNN) trained from scratch.

## How it works

1. Loads a small sample of the classic Kaggle Cats vs Dogs dataset (1,000 training images, 400 test images)
2. Applies data augmentation (rescaling, random flip, rotation, zoom) to reduce overfitting
3. Trains a CNN (`Conv2D` → `MaxPooling2D` → `Conv2D` → `MaxPooling2D` → `Dense`) to classify images
4. Uses early stopping to automatically halt training once validation accuracy stops improving
5. Saves the trained model so predictions can be made later without retraining
6. Includes a separate script to predict the class of any image using the saved model

## Requirements

- Python 3.9+
- TensorFlow

## Getting started

Clone the repo:

```bash
git clone https://github.com/IswaryaRama/pet-classifier.git
cd pet-classifier
```

(Optional but recommended) create a virtual environment:

```bash
python -m venv venv
```

Activate it:

- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```
- **Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```
  > If you get a "running scripts is disabled" error, run this first: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Dataset setup

The dataset is **not included** in this repo. Download a small sample (32.6 MB, 1,000 train / 400 test images) from Zenodo:

- **macOS / Linux:**
  ```bash
  curl -L -o catsdogs_small.zip "https://zenodo.org/records/5226945/files/cats_dogs_light.zip?download=1"
  unzip catsdogs_small.zip -d .
  mv cats_dogs_light dataset
  ```
- **Windows (PowerShell):**
  ```powershell
  Invoke-WebRequest -Uri "https://zenodo.org/records/5226945/files/cats_dogs_light.zip?download=1" -OutFile "catsdogs_small.zip"
  Expand-Archive catsdogs_small.zip -DestinationPath .
  Rename-Item "cats_dogs_light" "dataset"
  ```

> The zip extracts into its own folder (e.g. `cats_dogs_light`), not `dataset` — rename it as shown above so it matches the paths used in `pet.py` and `organize_pets.py`. Run `Get-ChildItem -Directory` (Windows) or `ls` (macOS/Linux) first if you're not sure of the extracted folder's exact name.

The extracted images sit flat inside `train/` and `test/` folders (e.g. `cat.0.jpg`, `dog.5.jpg`), rather than sorted into class subfolders. Run the organizing script to sort them into `cats/` and `dogs/` subfolders as required by `image_dataset_from_directory`:

```bash
python organize_pets.py
```

After this, your folder structure should look like:

```
pet-classifier/
├── pet.py
├── organize_pets.py
├── predict.py
├── requirements.txt
├── README.md
├── .gitignore
└── dataset/
    ├── train/
    │   ├── cats/
    │   └── dogs/
    └── test/
        ├── cats/
        └── dogs/
```

## Training

To create a `test.jpg` for a quick sanity check:

```powershell
$file = Get-ChildItem dataset\test\cats | Select-Object -First 1
Copy-Item $file.FullName "test.jpg"
```

Run the training script:

```bash
python pet.py
```

This will:
- Train the CNN for up to 10 epochs (early stopping may end it sooner)
- Print validation accuracy after each epoch
- Save the trained model as `pet_model.keras`
- Predict the class of `test.jpg` (make sure this file exists — see below)


## Predicting new images

Once `pet_model.keras` has been created, you don't need to retrain to test more images. Use the standalone prediction script instead:

```bash
python predict.py path/to/image.jpg
```

If no path is given, it defaults to `test.jpg`:

```bash
python predict.py
```

Example output:

```
Prediction: cats
```

## Notes

- This dataset is intentionally small for fast experimentation, so expect accuracy in the ~65–75% range rather than state-of-the-art results.
- To improve accuracy: use more training data, add stronger augmentation, or switch to transfer learning with a pretrained model (e.g. MobileNetV2) instead of training a CNN from scratch.
- GPU acceleration is not available on native Windows for TensorFlow 2.11+. Training runs on CPU unless you use WSL2 or the TensorFlow-DirectML plugin.

## License

MIT (or update to your preferred license)
