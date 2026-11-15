import subprocess, sys
subprocess.run([sys.executable, "scripts/generate_data.py"], check=True)
subprocess.run([sys.executable, "scripts/train_model.py"], check=True)
print("SentinelPay demo pipeline completed.")
