package helpers

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"

	"github.com/google/uuid"
	"golang.org/x/xerrors"
)

type Config struct {
	MLModelPath string `json:"ml_model_path"`
}

func GetConfig() (*Config, error) {
	jsonFile, err := os.Open(filepath.Join(os.Getenv("HOME"), ".machine-learning-models", "config.json"))
	if err != nil {
		return nil, xerrors.Errorf("failed to open config file: %w", err)
	}
	defer jsonFile.Close()

	byteValue, err := ioutil.ReadAll(jsonFile)
	if err != nil {
		return nil, xerrors.Errorf("failed to read config file: %w", err)
	}

	var config Config
	err = json.Unmarshal(byteValue, &config)
	if err != nil {
		return nil, xerrors.Errorf("failed to parse config file: %w", err)
	}

	return &config, nil
}

func GenerateRandomUUID() (string, error) {
	uuidStr, err := uuid.NewRandom()
	if err != nil {
		return "", xerrors.Errorf("failed to generate random UUID: %w", err)
	}
	return uuidStr.String(), nil
}

func EnsureDirectoryExists(dir string) error {
	err := os.MkdirAll(dir, os.ModePerm)
	if err != nil {
		return xerrors.Errorf("failed to create directory: %w", err)
	}
	return nil
}

func LogError(err error) {
	log.Printf("ERROR: %s", err.Error())
}

func LogInfo(msg string) {
	log.Printf("INFO: %s", msg)
}

func GenerateKey(size int) ([]byte, error) {
	key := make([]byte, size)
	_, err := rand.Read(key)
	if err != nil {
		return nil, xerrors.Errorf("failed to generate random key: %w", err)
	}
	return key, nil
}

func LoadMLModel(modelPath string) (interface{}, error) {
	// Assuming the ML model is loaded from a file
	bytes, err := ioutil.ReadFile(modelPath)
	if err != nil {
		return nil, xerrors.Errorf("failed to read ML model file: %w", err)
	}
	return bytes, nil
}