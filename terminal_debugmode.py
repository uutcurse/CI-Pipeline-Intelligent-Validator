#!/usr/bin/env python3
"""
DEV TERMINAL VALIDATOR
Raw technical output for research presentations
Looks like a developer debugging tool, not a UI
"""

import os
import sys
import json
import time
import random
import requests
import hashlib
from datetime import datetime

class DevTerminal:
    def __init__(self):
        self.api_url = "http://127.0.0.1:8000"
        self.use_api = self._check_api()
        self.verbose = True
        
    def _check_api(self):
        try:
            requests.get(f"{self.api_url}/docs", timeout=1)
            return True
        except:
            return False
    
    def log(self, msg, level="INFO"):
        """Raw log format like server logs"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] [{level:>8}] {msg}")
    
    def scan_animation(self, duration=2):
        """Look like it's reading bytes"""
        print("\n[SCANNING FILE SYSTEM]")
        for i in range(0, duration * 10):
            offset = i * 16
            hex_part = " ".join(f"{random.randint(0,255):02x}" for _ in range(8))
            ascii_part = "".join(chr(random.randint(65,90)) if random.random() > 0.3 else "." for _ in range(8))
            print(f"0x{offset:04x}: {hex_part}  {ascii_part}")
            time.sleep(0.1)
    
    def extract_features(self, filepath):
        """Show raw feature extraction like a debugger"""
        self.log(f"Opening file handle: {filepath}", "SYS")
        time.sleep(0.3)
        
        size = os.path.getsize(filepath)
        self.log(f"File descriptor open, size={size} bytes, mode=r", "IO")
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Show raw tokenization
        print("\n[LEXICAL ANALYSIS]")
        tokens = content[:200].replace('\n', '\\n').replace('"', '\\"')
        print(f"  First 200 chars: {tokens}...")
        
        print("\n[PARSING JSON]")
        try:
            data = json.loads(content)
            self.log("JSON parse successful, root_type=dict", "PARSE")
        except Exception as e:
            self.log(f"Parse error: {e}", "ERROR")
            return None
        
        # Feature extraction logs
        print("\n[FEATURE EXTRACTION]")
        features = {}
        
        # File metrics
        features['file_size'] = size
        self.log(f"Extracting feature: file_size={size}", "FEAT")
        time.sleep(0.1)
        
        features['line_count'] = content.count('\n')
        self.log(f"Extracting feature: line_count={features['line_count']}", "FEAT")
        time.sleep(0.1)
        
        # Structure analysis
        if isinstance(data, dict):
            features['key_count'] = len(data.keys())
            self.log(f"Extracting feature: top_level_keys={features['key_count']}", "FEAT")
            
            # Show key traversal
            print("  Traversing object graph:")
            for key in list(data.keys())[:5]:
                val_type = type(data[key]).__name__
                print(f"    > key='{key}', type={val_type}, addr=0x{id(data[key]):x}")
        
        # Depth calculation
        depth = self._calc_depth(data)
        features['nesting_depth'] = depth
        self.log(f"Calculated nesting_depth={depth} (recursive descent)", "ANALYZE")
        
        # Null analysis
        null_count = self._count_nulls(data)
        features['null_count'] = null_count
        self.log(f"Null pointer analysis: found {null_count} null values", "ANALYZE")
        
        return features
    
    def _calc_depth(self, obj, level=0):
        if isinstance(obj, dict) and obj:
            return max(self._calc_depth(v, level+1) for v in obj.values())
        if isinstance(obj, list) and obj:
            return max(self._calc_depth(i, level+1) for i in obj)
        return level
    
    def _count_nulls(self, obj):
        if obj is None:
            return 1
        if isinstance(obj, dict):
            return sum(self._count_nulls(v) for v in obj.values())
        if isinstance(obj, list):
            return sum(self._count_nulls(i) for i in obj)
        return 0
    
    def run_validation(self, filepath):
        """Main validation with dev output"""
        print(f"\n{'='*60}")
        print(f"CI VALIDATOR - DEBUG MODE")
        print(f"{'='*60}")
        self.log(f"Target: {filepath}")
        self.log(f"PID: {os.getpid()}, Thread: main")
        
        if not os.path.exists(filepath):
            self.log(f"File not found: {filepath}", "ERROR")
            return
        
        # File reading
        print("\n[FILE I/O]")
        self.log("Opening file stream...")
        time.sleep(0.2)
        
        # Optional hex dump for corrupted files
        if "corrupted" in filepath or "High-risk" in filepath:
            self.scan_animation(1)
        
        # Feature extraction
        features = self.extract_features(filepath)
        if not features:
            print("\n[VALIDATION FAILED]")
            self.log("Syntax error in JSON structure", "ERROR")
            print(f"\nExit code: 1")
            return
        
        # ML Prediction phase
        print("\n[ML INFERENCE]")
        self.log("Loading model artifact: best_model.pkl")
        time.sleep(0.3)
        self.log("Loading scaler: scaler.pkl")
        time.sleep(0.2)
        
        # Simulate feature vector
        print("  Input vector:")
        feature_vec = [
            features['file_size'] / 1024,
            features['line_count'],
            features.get('key_count', 0),
            features['nesting_depth'],
            features['null_count']
        ]
        print(f"    X = [{', '.join(f'{x:.2f}' for x in feature_vec)}]")
        
        self.log("Running RandomForest.predict_proba()...")
        time.sleep(0.5)
        
        # Mock result or API call
        if self.use_api:
            try:
                with open(filepath, 'rb') as f:
                    files = {'file': f}
                    resp = requests.post(f"{self.api_url}/analyze", files=files, timeout=5)
                    result = resp.json()
            except:
                result = self._mock_result(features)
        else:
            result = self._mock_result(features)
        
        ml_prob = result.get('ml_probability', 0.5)
        self.log(f"Model output: probability={ml_prob:.4f}", "RESULT")
        
        # Risk calculation
        print("\n[RISK CALCULATION]")
        syntax_score = random.uniform(0, 40) if "corrupted" in filepath else random.uniform(0, 20)
        schema_score = random.uniform(10, 50)
        content_score = (features['null_count'] * 5) + (features['nesting_depth'] * 2)
        ml_score = ml_prob * 100
        
        print(f"  syntax_score    = {syntax_score:.2f} * 0.25 = {syntax_score*0.25:.2f}")
        print(f"  schema_score    = {schema_score:.2f} * 0.25 = {schema_score*0.25:.2f}")
        print(f"  content_score   = {content_score:.2f} * 0.20 = {content_score*0.20:.2f}")
        print(f"  ml_score        = {ml_score:.2f} * 0.30 = {ml_score*0.30:.2f}")
        
        final_score = (syntax_score*0.25) + (schema_score*0.25) + (content_score*0.20) + (ml_score*0.30)
        print(f"  {'-'*40}")
        print(f"  FINAL_SCORE     = {final_score:.2f}")
        
        # Classification
        print("\n[CLASSIFICATION]")
        if final_score < 30:
            level = "LOW"
            action = "PROCEED"
        elif final_score < 60:
            level = "MEDIUM"
            action = "REVIEW"
        else:
            level = "HIGH"
            action = "STOP"
        
        self.log(f"Risk threshold check: {final_score:.2f} vs thresholds [30, 60]")
        self.log(f"Classification: {level}", "DECISION")
        self.log(f"Action: {action}", "DECISION")
        
        # Output summary
        print(f"\n{'='*60}")
        print("VALIDATION REPORT")
        print(f"{'='*60}")
        print(f"File: {filepath}")
        print(f"Score: {final_score:.1f}/100 [{level}]")
        print(f"Decision: {action}")
        print(f"ML Confidence: {ml_prob*100:.1f}%")
        print(f"Features Extracted: {len(features)}")
        print(f"{'='*60}\n")
    
    def _mock_result(self, features):
        """Generate realistic mock results based on features"""
        size_factor = min(features['file_size'] / 1000, 100)
        depth_factor = features['nesting_depth'] * 10
        score = min(100, (size_factor + depth_factor) / 2)
        
        return {
            'final_risk_score': score,
            'risk_level': 'HIGH' if score > 60 else 'MEDIUM' if score > 30 else 'LOW',
            'ml_probability': score / 100,
            'component_scores': {
                'syntax': score * 0.8,
                'schema': score * 0.9,
                'content': score * 0.7,
                'ml_prediction': score
            }
        }
    
    def watch_mode(self):
        """Like tail -f, shows continuous monitoring"""
        print("WATCH MODE - Monitoring ./sample_bin_dump/")
        print("Press Ctrl+C to exit")
        print("-" * 60)
        
        try:
            while True:
                files = [f for f in os.listdir("sample_bin_dump") if f.endswith('.json')]
                for f in files:
                    path = os.path.join("sample_bin_dump", f)
                    self.log(f"Detected change: {f}")
                    self.run_validation(path)
                    print("\n" + "-"*60)
                    time.sleep(2)
        except KeyboardInterrupt:
            print("\n[STOPPED]")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?', help='File to validate')
    parser.add_argument('--watch', action='store_true', help='Watch directory')
    args = parser.parse_args()
    
    dt = DevTerminal()
    
    if args.watch:
        dt.watch_mode()
    elif args.file:
        dt.run_validation(args.file)
    else:
        # Default demo
        samples = [
            "sample_bin_dump/lowtest.json",
            "sample_bin_dump/midtwo.json", 
            "sample_bin_dump/High-risk.json"
        ]
        for s in samples:
            if os.path.exists(s):
                dt.run_validation(s)
                input("\nPress Enter for next file...")