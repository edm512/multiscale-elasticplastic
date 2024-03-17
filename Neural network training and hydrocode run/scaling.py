import numpy as np
def scaling(train_dataset, test_dataset):
	# Input data normalization
	Norm_SR = max(abs(train_dataset['strain_rate']))
	train_dataset['norm_sr'] = train_dataset['strain_rate']/Norm_SR
	test_dataset['norm_sr'] = test_dataset['strain_rate']/Norm_SR

	Norm_OldS3 = max(abs(train_dataset['old_S3']))
	train_dataset['norm_OldS3'] = train_dataset['old_S3']/Norm_OldS3
	test_dataset['norm_OldS3'] = test_dataset['old_S3']/Norm_OldS3

	Norm_OldP2 = max(abs(train_dataset['old_P2']))
	train_dataset['norm_OldP2'] = train_dataset['old_P2']/Norm_OldP2
	test_dataset['norm_OldP2'] = test_dataset['old_P2']/Norm_OldP2

	Norm_S3 = max(abs(train_dataset['S3']))
	train_dataset['norm_S3'] = train_dataset['S3']/Norm_S3
	test_dataset['norm_S3'] = test_dataset['S3']/Norm_OldS3

	Norm_P2 = max(abs(train_dataset['P2']))
	train_dataset['norm_P2'] = train_dataset['P2']/Norm_P2
	test_dataset['norm_P2'] = test_dataset['P2']/Norm_P2

	Norm_old_dS3dt = max(abs(train_dataset['old_dS3dt']))
	train_dataset['norm_old_dS3dt'] = train_dataset['old_dS3dt']/Norm_old_dS3dt
	test_dataset['norm_old_dS3dt'] = test_dataset['old_dS3dt']/Norm_old_dS3dt

	Norm_old_dP2dt = max(abs(train_dataset['old_dP2dt']))
	train_dataset['norm_old_dP2dt'] = train_dataset['old_dP2dt']/Norm_old_dP2dt
	test_dataset['norm_old_dP2dt'] = test_dataset['old_dP2dt']/Norm_old_dP2dt

	Norm_dS3dt = max(abs(train_dataset['dS3dt']))
	train_dataset['norm_dS3dt'] = train_dataset['dS3dt']/Norm_dS3dt
	test_dataset['norm_dS3dt'] = test_dataset['dS3dt']/Norm_dS3dt

	Norm_dP2dt = max(abs(train_dataset['dP2dt']))
	train_dataset['norm_dP2dt'] = train_dataset['dP2dt']/Norm_dP2dt
	test_dataset['norm_dP2dt'] = test_dataset['dP2dt']/Norm_dP2dt

	Norm_old_T = max(abs(train_dataset['old_T']))
	train_dataset['norm_old_T'] = train_dataset['old_T']/Norm_old_T
	test_dataset['norm_old_T'] = test_dataset['old_T']/Norm_old_T

	Norm_dTdt = max(abs(train_dataset['dTdt']))
	train_dataset['norm_dTdt'] = train_dataset['dTdt']/Norm_dTdt
	test_dataset['norm_dTdt'] = test_dataset['dTdt']/Norm_dTdt

	Norm_voidSize = max(abs(train_dataset['voidSize']))
	train_dataset['norm_voidSize'] = train_dataset['voidSize']/Norm_voidSize
	test_dataset['norm_voidSize'] = test_dataset['voidSize']/Norm_voidSize

	scalings = np.array([Norm_OldS3, Norm_OldP2, Norm_SR, Norm_old_T, Norm_voidSize, Norm_dS3dt, Norm_dP2dt, Norm_dTdt])

	return scalings, train_dataset, test_dataset
