from ultralytics import YOLO
import os
import torch

def main():
    # Verifica se CUDA è disponibile e imposta il dispositivo
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print("Using device:", device)

    # Load the model.
    model = YOLO('yolov8n.pt').to(device)  # Sposta il modello sulla GPU se disponibile

    data_path = os.path.join(os.getcwd(), "dataset/data.yaml")

    # Training.
    results = model.train(
        data=data_path,
        imgsz=640,
        epochs=75,
        batch=8,
        name='yolov8_custom',
        device=device  # Specifica il dispositivo per l'addestramento
    )

if __name__ == '__main__':
    main()