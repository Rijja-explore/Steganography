from PIL import Image, PngImagePlugin
import base64

def embed_two_layer_ctf(cover_file, output_file, message_line, flag):
    """
    Embed a first-line message and a second-line Base64-encoded flag
    into PNG metadata for a two-layer CTF challenge.
    """
    # Encode the flag in Base64
    flag_encoded = base64.b64encode(flag.encode()).decode()

    # Open cover image
    img = Image.open(cover_file)

    # Add metadata chunks
    meta = PngImagePlugin.PngInfo()
    meta.add_text("Line1", message_line)    # visible welcome message
    meta.add_text("Line2", flag_encoded)    # second-layer Base64 flag

    # Save the stego image
    img.save(output_file, "PNG", pnginfo=meta)
    print(f"✅ Saved {output_file} with two-layer payload.")
    print("Players will decode Line1 for message, then Base64-decode Line2 for the flag.")

if __name__ == "__main__":
    cover_image = "Sample.jpg"  # Your base image
    output_image = "stego_chase.png"
    message_line = "CTF{ssn-snuc_invente_day}"
    flag = "https://github.com/cipherchase2627/elitespark-shelved"

    embed_two_layer_ctf(cover_image, output_image, message_line, flag)
