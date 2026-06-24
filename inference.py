import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

CLASS_NAMES = [
    'Acetaminophen', 'Aspirin', 'Ciprofloxacin',
    'Dexibuprofen', 'Famotidine', 'Ibuprofen',
    'Itraconazole', 'Lamotrigine', 'Loperamide',
    'MagnesiumHydroxide', 'Naproxen',
    'Nizatidine', 'Warfarin'
]

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])


def load_model(model_path='best_pill_model.pth'):
    model = models.resnet50(weights=None)

    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, len(CLASS_NAMES))

    model.load_state_dict(
        torch.load(model_path, map_location=DEVICE)
    )

    model.to(DEVICE)
    model.eval()

    return model


def predict_image(model, image_path):
    image = Image.open(image_path).convert('RGB')
    image = transform(image)
    image = image.unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = model(image)
        _, pred = torch.max(outputs, 1)

    return CLASS_NAMES[pred.item()]