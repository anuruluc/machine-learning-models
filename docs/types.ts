// types.ts
import { Model } from 'achine-learning-models/model';

export type Config<T extends string = string> = {
  model: Model;
  // add more properties as needed
};

export type CustomConfig = Config<'custom'> & {
  customProp: string;
};

export type LinearRegressionConfig = Config<'linear-regression'> & {
  learningRate: number;
  iterations: number;
};

export type NeuralNetworkConfig = Config<'neural-network'> & {
  hiddenLayers: number[];
  epochs: number;
};