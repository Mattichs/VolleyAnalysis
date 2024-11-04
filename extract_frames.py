import cv2
import os
import random

def extract_random_frames(video_path, output_dir, num_frames=500):
    # Crea la directory di output se non esiste
    os.makedirs(output_dir, exist_ok=True)

    # Apri il video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Errore: impossibile aprire il video.")
        return

    # Ottieni il numero totale di frame
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Numero totale di frame nel video: {total_frames}")

    # Genera una lista di frame casuali
    random_frames = random.sample(range(total_frames), min(num_frames, total_frames))

    # Estrai i frame casuali e salvali
    for frame_number in random_frames:
        # Imposta la posizione del frame corrente
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()
        if ret:
            # Salva il frame
            frame_filename = os.path.join(output_dir, f"frame_{frame_number:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Frame salvato: {frame_filename}")
        else:
            print(f"Errore: impossibile leggere il frame {frame_number}")

    # Rilascia il video
    cap.release()
    print("Estrazione completata.")

# Percorso del video e directory di output
video_path = "input/video.mp4"  # Sostituisci con il percorso del tuo video
output_dir = "output_frames"  # Sostituisci con la directory desiderata

# Esegui la funzione per estrarre i frame
extract_random_frames(video_path, output_dir)
